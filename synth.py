import os
import SimpleAudio as SA
import argparse
from nltk.corpus import cmudict
import re

### NOTE: DO NOT CHANGE ANY OF THE EXISITING ARGUMENTS
parser = argparse.ArgumentParser(
    description='A basic text-to-speech app that synthesises an input phrase using monophone unit selection.')
parser.add_argument('--monophones', default="monophones", help="Folder containing monophone wavs")
parser.add_argument('--play', '-p', action="store_true", default=False, help="Play the output audio")
parser.add_argument('--outfile', '-o', action="store", dest="outfile", type=str, help="Save the output audio to a file",
                    default=None)
parser.add_argument('phrase', nargs='+', help="The phrase to be synthesised")

# Arguments for extensions
parser.add_argument('--spell', '-s', action="store_true", default=False,
                    help="Spell the phrase instead of pronouncing it")
parser.add_argument('--volume', '-v', default=None, type=float,
                    help="A float between 0.0 and 1.0 representing the desired volume")

args = parser.parse_args()


class Synth(object):
    def __init__(self, wav_folder):
        self.phones = {}
        self.get_wavs(wav_folder)

    def get_wavs(self, wav_folder):
        for root, dirs, files in os.walk(wav_folder, topdown=False):
            for file in files:
                pass  # delete this line and implement


def get_phone_seq(phrase):
    pass  # delete this line and implement


if __name__ == "__main__":
    S = Synth(wav_folder=args.monophones)
    # out is the Audio object which will become your output
    # you need to modify S.data to produce the correct synthesis
    out = SA.Audio(rate=16000)

    phone_seq = get_phone_seq(args.phrase)
