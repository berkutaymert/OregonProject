#!/bin/bash

#SBATCH -o ./job.out.%j
#SBATCH -e ./job.err.%j

#SBATCH -D ./

#SBATCH -J kilo

#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=18
#SBATCH --mem=125000

#SBATCH --time=1-00:00:00

#SBATCH --mail-type=END
#SBATCH --mail-user=berkutay_mert@psych.mpg.de

module load anaconda/3/2021.11

python -m ks.py
