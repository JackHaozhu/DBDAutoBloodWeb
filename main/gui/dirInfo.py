import winreg
import os


def get_program_install_location(program_name):
    uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
    for i in range(0, winreg.QueryInfoKey(uninstall_key)[0]):
        subkey_name = winreg.EnumKey(uninstall_key, i)
        subkey = winreg.OpenKey(uninstall_key, subkey_name)
        try:
            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
            if (program_name in display_name) and os.path.exists(install_location):
                return install_location
        except FileNotFoundError:
            pass
        finally:
            subkey.Close()
    uninstall_key.Close()
    return None

character = {
    'TheTrapper': 'K01_TheTrapper_Portrait.png',
    'TheWraith': 'K02_TheWraith_Portrait.png',
    'TheHillbilly': 'K03_TheHillbilly_Portrait.png',
    'TheNurse': 'K04_TheNurse_Portrait.png',
    'DwightFairfield': 'S01_DwightFairfield_Portrait.png',
    'MegThomas': 'S02_MegThomas_Portrait.png',
    'ClaudetteMorel': 'S03_ClaudetteMorel_Portrait.png',
    'JakePark': 'S04_JakePark_Portrait.png',
    'NeaKarlsson': 'S05_NeaKarlsson_Portrait.png',
    'TheUnknown': 'Applepie\K35_TheUnknown_Portrait.png',
    'SableWard': 'Applepie\S41_SableWard_Portrait.png',
    'AshleyJWilliams': 'Ash\S17_AshleyJWilliams_Portrait.png',
    'TheTwins': 'Aurora\K22_TheTwins_Portrait.png',
    'ElodieRakoto': 'Aurora\S24_ElodieRakoto_Portrait.png',
    'TheCannibal': 'Cannibal\K09_TheCannibal_Portrait.png',
    'TheTrickster': 'Comet\K23_TheTrickster_Portrait.png',
    'YunJinLee': 'Comet\S25_YunJinLee_Portrait.png',
    'TheShape': 'DLC2\K06_TheShape_Portrait.png',
    'LaurieStrode': 'DLC2\S06_LaurieStrode_Portrait.png',
    'TheHag': 'DLC3\K05_TheHag_Portrait.png',
    'AceVisconti': 'DLC3\S07_AceVisconti_Portrait.png',
    'TheDoctor': 'DLC4\K07_TheDoctor_Portrait.png',
    'FengMin': 'DLC4\S09_FengMin_Portrait.png',
    'TheHuntress': 'DLC5\K08_TheHuntress_Portrait.png',
    'DavidKing': 'DLC5\S10_DavidKing_Portrait.png',
    'TheNemesis': 'Eclipse\K24_TheNemesis_Portrait.png',
    'JillValentine': 'Eclipse\S26_JillValentine_Portrait.png',
    'LeonSKennedy': 'Eclipse\S27_LeonSKennedy_Portrait.png',
    'TheNightmare': 'England\K10_TheNightmare_Portrait.png',
    'QuentinSmith': 'England\S11_QuentinSmith_Portrait.png',
    'ThePig': 'Finland\K11_ThePig_Portrait.png',
    'DetectiveDavidTapp': 'Finland\S12_DetectiveDavidTapp_Portrait.png',
    'TheCenobite': 'Gemini\K25_TheCenobite_Portrait.png',
    'TheClown': 'Guam\K12_TheClown_Portrait.png',
    'KateDenson': 'Guam\S13_KateDenson_Portrait.png',
    'TheSpirit': 'Haiti\K13_TheSpirit_Portrait.png',
    'AdamFrancis': 'Haiti\S14_AdamFrancis_Portrait.png',
    'MikaelaReid': 'Hubble\S28_MikaelaReid_Portrait.png',
    'TheArtist': 'Ion\K26_TheArtist_Portrait.png',
    'JonahVasquez': 'Ion\S29_JonahVasquez_Portrait.png',
    'TheLegion': 'Kenya\K14_TheLegion_Portrait.png',
    'JeffJohansen': 'Kenya\S15_JeffJohansen_Portrait.png',
    'TheOnryo': 'Kepler\K27_TheOnryo_Portrait.png',
    'YoichiAsakawa': 'Kepler\S30_YoichiAsakawa_Portrait.png',
    'WilliamBillOverbeck': 'L4D\S08_WilliamBillOverbeck_Portrait.png',
    'ThePlague': 'Mali\K15_ThePlague_Portrait.png',
    'JaneRomero': 'Mali\S16_JaneRomero_Portrait.png',
    'TheDredge': 'Meteor\K28_TheDredge_Portrait.png',
    'HaddieKaur': 'Meteor\S31_HaddieKaur_Portrait.png',
    'TheGhostface': 'Oman\K16_TheGhostface_Portrait.png',
    'TheMasterMind': 'Orion\K29_TheMasterMind_Portrait.png',
    'AdaWong': 'Orion\S32_AdaWong_Portrait.png',
    'RebeccaChambers': 'Orion\S33_RebeccaChambers_Portrait.png',
    'TheDemogorgon': 'Qatar\K17_TheDemogorgon_Portrait.png',
    'SteveHarrington': 'Qatar\S18_SteveHarrington_Portrait.png',
    'NancyWheeler': 'Qatar\S19_NancyWheeler_Portrait.png',
    'TheKnight': 'Quantum\K30_TheKnight_Portrait.png',
    'VittorioToscano': 'Quantum\S34_VittorioToscano_Portrait.png',
    'TheSkullMerchant': 'Saturn\K31_TheSkullMerchant_Portrait.png',
    'ThalitaLyra': 'Saturn\S35_ThalitaLyra_Portrait.png',
    'RenatoLyra': 'Saturn\S36_RenatoLyra_Portrait.png',
    'TheOni': 'Sweden\K18_TheOni_Portrait.png',
    'YuiKimura': 'Sweden\S20_YuiKimura_Portrait.png',
    'TheDeathslinger': 'Ukraine\K19_TheDeathslinger_Portrait.png',
    'ZarinaKassir': 'Ukraine\S21_ZarinaKassir_Portrait.png',
    'TheSingularity': 'Umbra\K32_TheSingularity_Portrait.png',
    'GabrielSoma': 'Umbra\S37_GabrielSoma_Portrait.png',
    'NicolasCage': 'Venus\S38_NicolasCage_Portrait.png',
    'TheExecutioner': 'Wales\K20_TheExecutioner_Portrait.png',
    'CherylMason': 'Wales\S22_CherylMason_Portrait.png',
    'TheXenomorph': 'Wormhole\K33_TheXenomorph_Portrait.png',
    'EllenRipley': 'Wormhole\S39_EllenRipley_Portrait.png',
    'TheBlight': 'Yemen\K21_TheBlight_Portrait.png',
    'FelixRichter': 'Yemen\S23_FelixRichter_Portrait.png',
    'TheYerkes': 'Yerkes\K34_TheYerkes_Portrait.png',
    'AlanWake': 'Zodiac\S40_AlanWake_Portrait.png'
}
# 图像有效面积255x335
killer_key = [
    'TheTrapper', 'TheWraith', 'TheHillbilly', 'TheNurse',
    'TheShape', 'TheHag', 'TheDoctor', 'TheHuntress',
    'TheCannibal', 'TheNightmare', 'ThePig', 'TheClown',
    'TheSpirit', 'TheLegion', 'ThePlague', 'TheGhostface',
    'TheDemogorgon', 'TheOni', 'TheDeathslinger', 'TheExecutioner',
    'TheBlight', 'TheTwins', 'TheTrickster', 'TheNemesis',
    'TheCenobite', 'TheArtist', 'TheOnryo', 'TheDredge',
    'TheMasterMind', 'TheKnight', 'TheSkullMerchant', 'TheSingularity',
    'TheXenomorph', 'TheYerkes', 'TheUnknown'
]

human_key = [
    'DwightFairfield', 'MegThomas', 'ClaudetteMorel', 'JakePark',
    'NeaKarlsson', 'LaurieStrode', 'AceVisconti', 'BillOverbeck',
    'FengMin', 'DavidKing', 'QuentinSmith', 'DavidTapp',
    'KateDenson', 'AdamFrancis', 'JeffJohansen', 'JaneRomero',
    'AshleyWilliams', 'NancyWheeler', 'SteveHarrington', 'YuiKimura',
    'ZarinaKassir', 'CherylMason', 'FelixRichter', 'ElodieRakoto',
    'YunJinLee', 'JillValentine', 'LeonSKennedy', 'MikaelaReid',
    'JonahVasquez', 'YoichiAsakawa', 'HaddieKaur', 'AdaWong',
    'RebeccaChambers', 'VittorioToscano', 'ThalitaLyra', 'RenatoLyra',
    'GabrielSoma', 'NicolasCage', 'EllenRipley', 'AlanWake',
    'SableWard'
]