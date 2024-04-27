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

character_path = {
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

easter_egg = {
    '这里什么也没有': '这里真的什么也没有',
    '这里真的什么也没有': '真的真的什么也没有哦',
    '真的真的什么也没有哦': '真的真的真的什么也没有哦',
    '真的真的真的什么也没有哦': '别再点啦(✿◠‿◠)',
    '别再点啦(✿◠‿◠)': '再点下去也不有别的东西的',
    '再点下去也不有别的东西的': '我要生气了哦(¬_¬ )',
    '我要生气了哦(¬_¬ )': '我真的要生气了哦<( ￣^￣)',
    '我真的要生气了哦<( ￣^￣)': '我真的真的要生气了哦(* ￣︿￣)',
    '我真的真的要生气了哦(* ￣︿￣)': '我真的真的真的要生气了哦(╬▔皿▔)╯',
    '我真的真的真的要生气了哦(╬▔皿▔)╯': '不陪你玩了(。>︿<)_θ',
    '不陪你玩了(。>︿<)_θ': '不陪你玩了(。>︿<)_θ'
}

offerings_path = {
    'ardentRavenWreath': 'iconFavors_ardentRavenWreath.png',
    'ardentShrikeWreath': 'iconFavors_ardentShrikeWreath.png',
    'ardentSpottedOwlWreath': 'iconFavors_ardentSpottedOwlWreath.png',
    'ardentTanagerWreath': 'iconFavors_ardentTanagerWreath.png',
    'azarovsKey': 'iconFavors_azarovsKey.png',
    'blackSaltStatuette': 'iconFavors_blackSaltStatuette.png',
    'bogLaurelSachet': 'iconFavors_bogLaurelSachet.png',
    'boundEnvelope': 'iconFavors_boundEnvelope.png',
    'cattleTag28': 'iconFavors_cattleTag28.png',
    'cattleTag81': 'iconFavors_cattleTag81.png',
    'chalkPouch': 'iconFavors_chalkPouch.png',
    'charredWeddingPhotograph': 'iconFavors_charredWeddingPhotograph.png',
    'clearReagent': 'iconFavors_clearReagent.png',
    'creamChalkPouch': 'iconFavors_creamChalkPouch.png',
    'crecentMoonBouquet': 'iconFavors_crecentMoonBouquet.png',
    'crispleafAmaranthSachet': 'iconFavors_crispleafAmaranthSachet.png',
    'cutCoin': 'iconFavors_cutCoin.png',
    'devoutRavenWreath': 'iconFavors_devoutRavenWreath.png',
    'devoutShrikeWreath': 'iconFavors_devoutShrikeWreath.png',
    'devoutSpottedOwlWreath': 'iconFavors_devoutSpottedOwlWreath.png',
    'devoutTanagerWreath': 'iconFavors_devoutTanagerWreath.png',
    'faintReagent': 'iconFavors_faintReagent.png',
    'fragrantBogLaurel': 'iconFavors_fragrantBogLaurel.png',
    'fragrantCrispleafAmaranth': 'iconFavors_fragrantCrispleafAmaranth.png',
    'fragrantPrimroseBlossom': 'iconFavors_fragrantPrimroseBlossom.png',
    'fragrantSweetWilliam': 'iconFavors_fragrantSweetWilliam.png',
    'freshBogLaurel': 'iconFavors_freshBogLaurel.png',
    'freshCrispleafAmaranth': 'iconFavors_freshCrispleafAmaranth.png',
    'freshPrimroseBlossom': 'iconFavors_freshPrimroseBlossom.png',
    'freshSweetWilliam': 'iconFavors_freshSweetWilliam.png',
    'fullMoonBouquet': 'iconFavors_fullMoonBouquet.png',
    'hazyReagent': 'iconFavors_hazyReagent.png',
    'heartLocket': 'iconFavors_heartLocket.png',
    'hollowShell': 'iconFavors_hollowShell.png',
    'ivoryChalkPouch': 'iconFavors_ivoryChalkPouch.png',
    'jarOfSaltyLips': 'iconFavors_jarOfSaltyLips.png',
    'lunacyTicket': 'iconFavors_lunacyTicket.png',
    'macmillianLedgerPage': 'iconFavors_macmillianLedgerPage.png',
    'macmilliansPhalanxBone': 'iconFavors_macmilliansPhalanxBone.png',
    'moldyOak': 'iconFavors_moldyOak.png',
    'momentoMoriCypress': 'iconFavors_momentoMoriCypress.png',
    'momentoMoriEbony': 'iconFavors_momentoMoriEbony.png',
    'momentoMoriIvory': 'iconFavors_momentoMoriIvory.png',
    'murkyReagent': 'iconFavors_murkyReagent.png',
    'newMoonBouquet': 'iconFavors_newMoonBouquet.png',
    'pElliottLunacyTicket': 'iconFavors_pElliottLunacyTicket.png',
    'petrifiedOak': 'iconFavors_petrifiedOak.png',
    'plateShredded': 'iconFavors_plateShredded.png',
    'plateVirginia': 'iconFavors_plateVirginia.png',
    'primroseBlossomSachet': 'iconFavors_primroseBlossomSachet.png',
    'putridOak': 'iconFavors_putridOak.png',
    'quarterMoonBouquet': 'iconFavors_quarterMoonBouquet.png',
    'ravenWreath': 'iconFavors_ravenWreath.png',
    'rottenOak': 'iconFavors_rottenOak.png',
    'saltPouch': 'iconFavors_saltPouch.png',
    'scratchedCoin': 'iconFavors_scratchedCoin.png',
    'sealedEnvelope': 'iconFavors_sealedEnvelope.png',
    'shinyCoin': 'iconFavors_shinyCoin.png',
    'shrikeWreath': 'iconFavors_shrikeWreath.png',
    'shroudOfBinding': 'iconFavors_shroudOfBinding.png',
    'shroudOfSeparation': 'iconFavors_shroudOfSeparation.png',
    'shroudOfUnion': 'iconFavors_shroudOfUnion.png',
    'signedLedgerPage': 'iconFavors_signedLedgerPage.png',
    'spottedOwlWreath': 'iconFavors_spottedOwlWreath.png',
    'sweetWilliamSachet': 'iconFavors_sweetWilliamSachet.png',
    'tanagerWreath': 'iconFavors_tanagerWreath.png',
    'tarnishedCoin': 'iconFavors_tarnishedCoin.png',
    'vigosShroud': 'iconFavors_vigosShroud.png',
    'wardBlack': 'iconFavors_wardBlack.png',
    'wardWhite': 'iconFavors_wardWhite.png',
    '4thAnniversary': 'Anniversary\iconFavors_4thAnniversary.png',
    'bloodyPartyStreamers': 'Anniversary\iconFavors_bloodyPartyStreamers.png',
    'escapeCake': 'Anniversary\iconFavors_escapeCake.png',
    'gruesomeGateau': 'Anniversary\iconFavors_gruesomeGateau.png',
    'survivorPudding': 'Anniversary\iconFavors_survivorPudding.png',
    '5thAnniversary': 'Anniversary\iconsFavors_5thAnniversary.png',
    '6thAnniversary': 'Anniversary\iconsFavors_6thAnniversary.png',
    '7thAnniversary': 'Anniversary\iconsFavors_7thAnniversary.png',
    'boneSplinter': 'Cannibal\iconFavors_boneSplinter.png',
    'blackSplinter': 'DLC2\iconFavors_blackSplinter.png',
    'decrepitClapboard': 'DLC2\iconFavors_decrepitClapboard.png',
    'harvestFestivalLeaflet': 'DLC2\iconFavors_harvestFestivalLeaflet.png',
    'strodeRealtyKey': 'DLC2\iconFavors_strodeRealtyKey.png',
    'fumingCordage': 'DLC3\iconFavors_fumingCordage.png',
    'fumingWelcomeSign': 'DLC3\iconFavors_fumingWelcomeSign.png',
    'granmasCookbook': 'DLC3\iconFavors_granmasCookbook.png',
    'muddySplinter': 'DLC3\iconFavors_muddySplinter.png',
    'emergencyCertificate': 'DLC4\iconFavors_emergencyCertificate.png',
    'psychiatricAssessmentReport': 'DLC4\iconFavors_psychiatricAssessmentReport.png',
    'shatteredGlasses': 'DLC4\iconFavors_shatteredGlasses.png',
    'shockSplinter': 'DLC4\iconFavors_shockSplinter.png',
    'childrensBook': 'DLC5\iconFavors_childrensBook.png',
    'paintedRiverRock': 'DLC5\iconFavors_paintedRiverRock.png',
    'theLastMask': 'DLC5\iconFavors_theLastMask.png',
    'RPDBadge': 'Eclipse\iconsFavors_RPDBadge.png',
    'smokingSplinter': 'England\iconFavors_smokingSplinter.png',
    'thePiedPiper': 'England\iconFavors_thePiedPiper.png',
    'glassSplinter': 'Finland\iconFavors_glassSplinter.png',
    'jigsawPiece': 'Finland\iconFavors_jigsawPiece.png',
    'yamaokasCrest': 'Haiti\iconFavors_yamaokasCrest.png',
    'pustulaPetals': 'Halloween\iconFavors_pustulaPetals.png',
    'CursedSeed': 'Halloween2021\iconFavors_CursedSeed.png',
    'ArcaneDowsingRod': 'Halloween2022\iconFavors_ArcaneDowsingRod.png',
    'crowsEye': 'Ion\iconFavors_crowsEye.png',
    'damagedPhoto': 'Kenya\iconFavors_damagedPhoto.png',
    'redMoneyPacket': 'LunarNewYear\iconFavors_redMoneyPacket.png',
    'IchorousLoam': 'Meteor\iconFavors_IchorousLoam.png',
    'hawkinsNationalLaboratoryID': 'Qatar\iconFavors_hawkinsNationalLaboratoryID.png',
    'BeefTallowMixture': 'Quantum\iconFavors_BeefTallowMixture.png',
    'bloodshotEye': 'Spring\iconFavors_bloodshotEye.png',
    'bbqInvitation': 'Summer\iconFavors_bbqInvitation.png',
    'dustyNoose': 'Ukraine\iconFavors_dustyNoose.png',
    'ShatteredBottle': 'Ukraine\iconFavors_ShatteredBottle.png',
    'alienFlora': 'Umbra\iconFavors_alienFlora.png',
    'marysLetter': 'Wales\iconFavors_marysLetter.png',
    'airlockDoors': 'Wormhole\iconFavors_airlockDoors.png',
    'annotatedBlueprint': 'Yemen\iconFavors_annotatedBlueprint.png',
    'bloodiedBlueprint': 'Yemen\iconFavors_bloodiedBlueprint.png',
    'tornBlueprint': 'Yemen\iconFavors_tornBlueprint.png',
    'vigosBlueprint': 'Yemen\iconFavors_vigosBlueprint.png',
    'wardSacrificial': 'Yemen\iconFavors_wardSacrificial.png',

}

offerings_rarity = {
    'killers': {
        ''
    }
}

offerings = {
    'killers': {
        'momentoMoriEbony': {
            'name': [
                '黑檀死亡坠链',
                'Ebony Momento Mori'
            ],
            'description': {
                '赐予你在下一次游戏中亲手处决所有进入第二层上钩状态的逃生者的能力。',
                'Grants the ability to kill all Survivors in the Dying State, who have progressed two Hook Stages.'
            }
        },
        'wardBlack': {
            'name': [
                '黑护符',
                'Black Ward'
            ],
            'description': {
                '燃烧这件祭品，可以在游戏中保护你免遭附加品的损失。',
                'Grants protection against the loss of your Add-ons at the end of the Trial.'
            }
        },
        'cutCoin': {
            'name': [
                '切分的硬币',
                'Cut Coin'
            ],
            'description': {
                '召唤恶灵，避免出现两个箱子。',
                'Calls upon The Entity to reduce the number of Chests by -2 Chests.'
            }
        },
        'murkyReagent': {
            'name': [
                '超强厚雾试剂',
                'Murky Reagent'
            ],
            'description': {
                '大幅增强黑雾。',
                'Increases the Thickness of the Dark Mist by +75 %.'
            }
        },
        'putridOak': {
            'name': [
                '朽坏的橡木',
                'Putrid Oak'
            ],
            'description': {
                '召唤恶灵大幅缩小献祭钩之间的间距。',
                'Calls upon The Entity to decrease the minimum Spawn distance between Hooks by -3.5 metres.'
            }
        }


    },
    'survivors': {
        'petrifiedOak': {
            'name': [
                '石化橡木',
                'Petrified Oak'
            ],
            'description': {
                '平息恶灵的怒火，小幅增加钩子之间出现的距离。',
                'Calms The Entity to increase the minimum Spawn distance between Hooks by +1 metre.'
            }
        },
        'shinyCoin': {
            'name': [
                '闪亮的硬币',
                'Shiny Coin'
            ],
            'description': {
                '召唤恶灵，多制造2个箱子。',
                'Calms The Entity to increase the number of Chests by +2 Chests.'
            }
        },
        'shroudOfBinding': {
            'name': [
                '捆绑裹尸布',
                'Shroud of Binding'
            ],
            'description': {
                '所有的逃生者进入游戏时位置集中。',
                'Calms the Entity to spawn all Survivors together.'
            }
        },
        'jarOfSaltyLips': {
            'name': [
                '威戈的盐渍唇罐',
                'Vigo\'s Jar of Salty Lips'
            ],
            'description': {
                '大幅增加所有逃生者的运气。',
                'Increases the Odds of every Survivor succeeding a Self-Unhook attempt by +3 %.'
            }
        },
        'wardWhite': {
            'name': [
                '白护符',
                'White Ward'
            ],
            'description': {
                '燃烧这件祭品，可以让你在死亡后免遭道具和附加品的损失。',
                'Grants protection against the loss of your Item and its Add-ons.'
            }
        }

    },
    'common': {

    }
}

addons = {
    'killers': {
        'TheTrapper': {},
        'TheWraith': {},
        'TheHillbilly': {},
        'TheNurse': {},
        'TheShape': {},
        'TheHag': {},
        'TheDoctor': {},
        'TheHuntress': {},
        'TheCannibal': {},
        'TheNightmare': {},
        'ThePig': {},
        'TheClown': {},
        'TheSpirit': {},
        'TheLegion': {},
        'ThePlague': {},
        'TheGhostface': {},
        'TheDemogorgon': {},
        'TheOni': {},
        'TheDeathslinger': {},
        'TheExecutioner': {},
        'TheBlight': {},
        'TheTwins': {},
        'TheTrickster': {},
        'TheNemesis': {},
        'TheCenobite': {},
        'TheArtist': {},
        'TheOnryo': {},
        'TheDredge': {},
        'TheMasterMind': {},
        'TheKnight': {},
        'TheSkullMerchant': {},
        'TheSingularity': {},
        'TheXenomorph': {},
        'TheYerkes': {},
        'TheUnknown': {}
    },
    'human':{

    }
}