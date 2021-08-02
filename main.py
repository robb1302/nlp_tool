import argparse

# TODO: correct help text for all arguments
# argparser
parser = argparse.ArgumentParser(
    description='', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument(
    '--data', help='Dataset to analyse', type=str, default='bank-additional-full.csv')
parser.add_argument(
    '--model', help='model to train', type=str, default='nn')

args = parser.parse_args()

# Fuehrt Funktionen aus Library mainFunction aus
if __name__ == '__main__':

    import shutil
    import timeit

    import src.utils.globals as GLOBALS
    from src.main_function.nlp_analyzer import nlp_analyzer

    start = timeit.default_timer()
    nlp_analyzer(
        data=args.data,
        model=args.model,

    )

    stop = timeit.default_timer()
    print('Time: ', round(stop - start, 0))
    # Cleanup
    shutil.rmtree(GLOBALS.TEMP_FOLDER)
    print('Temporary Folder deleted')
