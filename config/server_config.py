# -*- coding:utf-8 -*-
__author__ = 'xuan'

port = 8001
version = "1.0.0"
project_name = "auto_trader"


class ServerConfig:

    def __init__(self):
        self.port = 8000
        self._get_configurations()

    def _get_configurations(self):
        self.port = port
        self.version = version
        self.project_name = project_name


server_current_config = ServerConfig()
