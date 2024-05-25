
def change_name(choice_keys=None):
    local_atrs = {
        "steam": "❌Steam",
        "epic": "❌Epic",
        "riot": "❌Riot",
        "roblox": "❌Roblox",
        "ea": "❌EA",
        "battlenet": "❌Battle.Net",
        "supercell": "❌Supercell",
        "tarkov": "❌Tarkov",
        "ubisoft": "❌Ubisoft",
        "rockstar": "❌Rockstar",
        "mihoyo": "❌Mihoyo",
        "minecraft": "❌Minecraft",
        "pubg_mobile": "❌Pubg mobile",
        "albion": "❌Albion",
    }

    if choice_keys:
        for key in choice_keys:
            if key in local_atrs:
                if local_atrs[key][0] == "❌":
                    local_atrs[key] = local_atrs[key].replace("❌", "✅")
                elif local_atrs[key][0] == "✅":
                    local_atrs[key] = local_atrs[key].replace("✅", "❌")


    return local_atrs

