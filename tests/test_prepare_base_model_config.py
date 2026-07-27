from defect_detection.config.configuration import ConfigurationManager


def main():
    config = ConfigurationManager()

    prepare_config = config.get_prepare_base_model_config()

    print(prepare_config)


if __name__ == "__main__":
    main()