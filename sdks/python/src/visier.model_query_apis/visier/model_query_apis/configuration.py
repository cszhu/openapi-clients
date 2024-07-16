# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501
import base64
import copy
import hashlib
import http.client as httplib
import logging
import multiprocessing
import secrets
import sys
import threading
import time
import webbrowser
from logging import FileHandler
from queue import Queue, Empty
from typing import Optional
from urllib.parse import urljoin, quote, urlparse, urlencode
from wsgiref.simple_server import make_server

import requests
import urllib3
from flask import Flask, request

from visier.model_query_apis.exceptions import ApiException

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}


class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param ignore_operation_servers
      Boolean to ignore operation servers for the API client.
      Config will use `host` as the base url regardless of the operation servers.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = visier.model_query_apis.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123
    """

    _default = None

    def __init__(self,
                 host=None,
                 api_key=None,
                 api_key_prefix=None,
                 api_key_auth=None,
                 username=None,
                 password=None,
                 client_id=None,
                 client_secret=None,
                 redirect_uri=None,
                 target_tenant_id=None,
                 vanity=None,
                 scope=None,
                 access_token=None,
                 refresh_token=None,
                 token_expiration_time_secs=None,
                 server_index=None,
                 server_variables=None,
                 server_operation_index=None,
                 server_operation_variables=None,
                 ignore_operation_servers=False,
                 ssl_ca_cert=None,
                 retries=None,
                 *,
                 debug: Optional[bool] = None
                 ) -> None:
        """Constructor
        """

        self.token_expiration_secs = 3600 if token_expiration_time_secs is None else token_expiration_time_secs
        self.token_acquired_at = None

        self.refresh_token = refresh_token
        self.scope = scope or 'read'
        self.vanity = vanity
        self.target_tenant_id = target_tenant_id
        self.redirect_uri = redirect_uri
        self.client_secret = client_secret
        self.client_id = client_id
        self._base_path = "http://localhost" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key_auth = api_key_auth

        self.api_key = api_key
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = _default_refresh_config
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("visier.model_query_apis")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    def is_token_expired(self):
        return time.time() - self.token_acquired_at > self.token_expiration_secs

    @classmethod
    def get_default_copy(cls):
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls):
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        # Necessary key for all auth types
        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self, False)

        auth = {'ApiKeyAuth': {
            'type': 'api_key',
            'in': 'header',
            'key': 'apikey',
            'value': self.api_key_auth
        }}

        if self.access_token is not None:
            auth['BearerAuth'] = {
                'type': 'bearer',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        if 'CookieAuth' in self.api_key:
            auth['CookieAuth'] = {
                'type': 'api_key',
                'in': 'cookie',
                'key': 'VisierASIDToken',
                'value': self.get_api_key_with_prefix(
                    'CookieAuth',
                ),
            }
        if self.access_token is not None:
            auth['OAuth2Auth'] = {
                'type': 'oauth2',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        if self.access_token is not None:
            auth['OAuth2Auth'] = {
                'type': 'oauth2',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n" \
               "OS: {env}\n" \
               "Python Version: {pyversion}\n" \
               "Version of the API: 22222222.99201.1371\n" \
               "SDK Package Version: 1.0.0". \
            format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None


# Additional logic to extend default behaviour
########################################################################################################################


class CallbackServer:
    """Callback server that listens for the OAuth2 authorization code"""

    def __init__(self, provided_url: str) -> None:
        parsed_uri = urlparse(provided_url)
        self.host = parsed_uri.hostname or "localhost"
        self.port = parsed_uri.port or 5000
        self.path = parsed_uri.path or "/oauth2/callback"

        self.server = None
        self.flask_thread = None
        self.app = Flask(__name__)
        self.app.route(self.path, methods=["GET"])(self.callback)
        self.queue = Queue()

    def callback(self):
        """The handler for the OAuth2 callback providing the auth code"""
        code = request.args.get("code")
        self.queue.put(code)
        return "<p>You can now close this window</p>"

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, ex_type, ex_value, trace_back):
        self.stop()

    def start(self):
        """Starts the callback server"""
        self.server = make_server(self.host, self.port, self.app)
        self.flask_thread = threading.Thread(target=self.server.serve_forever)
        self.flask_thread.start()

    def stop(self):
        """Stops the callback server"""
        if self.server:
            self.server.shutdown()
            self.flask_thread.join()
            self.server = None
            self.flask_thread = None


def _post_request(url: str, data: dict, additional_headers: dict = None, auth=None):
    headers = {
        'Accept': 'application/jsonlines, application/json',
        'User-Agent': 'OpenAPI-python',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    if additional_headers:
        headers = {**headers, **additional_headers}
    # TODO currently using requests due some auth problems using urllib3
    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=auth
    )
    response.raise_for_status()
    return response


def _connect_asid(config):
    url = urljoin(config.host, '/v1/admin/visierSecureToken')
    data = {
        'username': config.username,
        'password': config.password
    }
    if config.vanity:
        data['vanityName'] = config.vanity
    response = _post_request(url=url, data=data)
    config.api_key['CookieAuth'] = f'VisierASIDToken={response.text}'


def _update_access_token(config: Configuration, body: dict):
    url = config.host + "/v1/auth/oauth2/token"
    if config.redirect_uri:
        body["redirect_uri"] = config.redirect_uri
    auth = (config.client_id, quote(config.client_secret, safe=''))
    headers = {
        "apikey": config.api_key["ApiKeyAuth"],
    }

    response = _post_request(url=url, data=body, additional_headers=headers, auth=auth)
    response_json = response.json()
    config.access_token = response_json.get('access_token')
    config.token_acquired_at = time.time()
    config.refresh_token = response_json.get('refresh_token')


def _refresh_token(config):
    body = {
        "grant_type": "refresh_token",
        "refresh_token": config.refresh_token,
    }
    _update_access_token(config, body)


def _connect_oauth_password(config):
    body = {
        "grant_type": "password",
        "client_id": config.client_id,
        "scope": config.scope,
        "username": config.username,
        "password": config.password,
    }
    _update_access_token(config, body)


def _connect_oauth_code(config):
    """Connect to Visier using (three-legged) OAuth2.
           This method will attempt to open a browser for the authentication and consent screens.
           It will also spin up a local web server to receive the OAuth2 authorization code."""
    code_verifier = secrets.token_urlsafe(64)
    code_challenge_digest = hashlib.sha256(code_verifier.encode()).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge_digest).decode().rstrip("=")

    url_prefix = config.host + "/v1/auth/oauth2"
    with CallbackServer(config.redirect_uri) as svr:
        query_args = {
            "apikey": config.api_key['ApiKeyAuth'],
            "response_type": "code",
            "client_id": config.client_id,
            "code_challenge_method": "S256",
            "code_challenge": code_challenge
        }
        if config.redirect_uri:
            query_args["redirect_uri"] = config.redirect_uri

        browser_url = f'{url_prefix}/authorize?{urlencode(query_args)}'
        # Launch the browser for authentication and consent screens
        webbrowser.open(browser_url)
        try:
            # Wait up to 2 minutes for the user to complete the OAuth2 code flow
            # TODO add timeouts
            code = svr.queue.get(block=True, timeout=120)
            body = {
                "grant_type": "authorization_code",
                "client_id": config.client_id,
                "scope": "read",
                "code": code,
                "code_verifier": code_verifier
            }
            _update_access_token(config, body)
            # self._update_session(get_token(code, code_verifier), self.configuration.api_key)
        except Empty as empty:
            raise ApiException("Timed out waiting for OAuth2 auth code") from empty


def _connect_oauth(config):
    if config.refresh_token:
        _update_access_token(config, {
            "grant_type": "refresh_token",
            "refresh_token": config.refresh_token,
        })
    elif config.username and config.password:
        _connect_oauth_password(config)
    else:
        _connect_oauth_code(config)


def _need_to_connect(config: Configuration):
    if config.client_id and config.client_secret:
        return not config.access_token or config.is_token_expired()

    if config.username and config.password:
        return not config.api_key.get('CookieAuth') or config.is_token_expired()

    raise ValueError("No valid authentication method found")


def _default_refresh_config(config: Configuration, force_refresh: bool):
    if not force_refresh and not _need_to_connect(config):
        return

    if config.client_id and config.client_secret:
        _connect_oauth(config)
    elif config.username and config.password:
        _connect_asid(config)
