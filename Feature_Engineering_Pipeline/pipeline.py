import utils

logs = utils.get_logger(__name__)

def run(
        export_end_reference_datetime: Optional[datetime.datetime] = None,
        days_delay: int = 15,
        days_export: int = 30,
        url: str = "https://www.energidataservice.dk/tso-electricity/ConsumptionDE35Hour",
        feature_group_version: int = 1,
        ) -> dict:
    
    """
    Extract data from the API
    Args:
        export_end_reference_datetime: The end reference datetime of the export window. If None, current time is used.
                                       Because the data is always delayed with "days_delay" days, this date is used only as  a reference point. The real extracted window will be computed as [export_end_reference_datetime - days_delay - days_export, export_end_reference_datetime - days_delay].
        days_delay: Data has a delay of N days. thus, we have to shift out window with N days.
        days_export: The number of days to export.
        url: The URL of the API.
        feature_group_version: The version of the feature store feature group to save teh data to.
    Returns:
        A dictionary containing metadata of the pipeline.
    """

    logger.info(f"Extracting data from API.")
    data, metadata = extract.from_api(
        export_end_reference_datetime, days_delay, days_export, url
    )
    logger.info("Successfully extracted data from API.")

