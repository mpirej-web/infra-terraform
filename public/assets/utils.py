import os
import sys
import logging
import logging.config
import yaml
from pathlib import Path

class TerraformConfig:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path

    def load(self):
        with open(self.config_file_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(f"YAML error: {exc}")
                sys.exit(1)

class FileUtil:
    @staticmethod
    def read_file(path: str) -> str:
        with open(path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(path: str, content: str):
        with open(path, 'w') as file:
            file.write(content)

    @staticmethod
    def rename_file(src: str, dst: str):
        try:
            os.rename(src, dst)
        except FileExistsError as e:
            print(f"File already exists: {e}")

class LoggingUtil:
    @staticmethod
    def configure_logger(config_path: str):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            logging.config.dictConfig(config)