from TradePilot.constants import *
from TradePilot.utils.common import create_directories, read_yaml
from TradePilot.entity.config_entity import PriceIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        data_config_filepath = DATA_CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH,
        ):

        self.config = read_yaml(config_filepath)
        self.data_config = read_yaml(data_config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_price_ingestion_config(self) -> PriceIngestionConfig:
        config = self.config.price_ingestion
        companies = self.data_config.Companies
        data_properties = self.data_config.DataFrame

        create_directories([config.root_dir])

        price_ingestion_config = PriceIngestionConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir,
            companies=companies,
            date_start=data_properties.start,
            date_end=data_properties.end,
            period=data_properties.period,
        )

        return price_ingestion_config