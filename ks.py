import kilosort
from kilosort.utils import download_probes
from kilosort import run_kilosort, DEFAULT_SETTINGS

download_probes()

settings = DEFAULT_SETTINGS
settings['n_chan_bin'] = 128

DB_probe = kilosort.io.load_probe("../DB0x2DP640x2D10D_kilosortChanMap.prb")

ops, st, clu, tF, Wall, similar_templates, is_ref, est_contam_rate, kept_spikes = run_kilosort(settings=settings,
             probe=DB_probe,
             filename='../062122_D/5546_thal_day2_Berk2/062122_5546_hf_fm_day2.bin',
             results_dir= 'Y:/Oregon Data/062122_D/5546_thal_day2_Berk2/kilosort4/try5',
             data_dtype="int16",
             do_CAR="False",
             )