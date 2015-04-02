import os
import logging

from libs.read import load_data
from libs.predictions import make_predictions
from libs.utils import safe_dirs

logger = logging.getLogger('predictions')


def predictions(args):
    """
    Create predictions of clusters
    """

    logger.info("reading sequeces")
    data = load_data(args.json)
    out_dir = os.path.join(args.out, "predictions")
    safe_dirs(out_dir)

    logger.info("make predictions")
    make_predictions(data, out_dir, args)

    logger.info("Done")
