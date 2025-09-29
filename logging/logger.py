import logging

# configure
logging.basicConfig(
    filename="app.log",  # logs in a file
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # to format the log msgs
)
