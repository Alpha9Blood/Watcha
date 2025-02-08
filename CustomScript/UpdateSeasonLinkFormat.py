from Script.ManageData.Anime.ManageSeasons import SeasonManager
from Script.Utils import JsonUtil


class UpdateSeasonLinkFormat:
    def __init__(self) -> None:
        pass

    def OverrideFormat(self):
        OldSeasonFormat:dict[str, str] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
        NewSeasonFormat:dict[str, dict[str, str]] = {}

        for Season in OldSeasonFormat:
            if (str(SeasonManager.GetSeasonYear(Season)) not in NewSeasonFormat):
                NewSeasonFormat.update({str(SeasonManager.GetSeasonYear(Season)): {Season: OldSeasonFormat[Season]}})
            else:
                NewSeasonFormat[str(SeasonManager.GetSeasonYear(Season))].update({Season: OldSeasonFormat[Season]})

        JsonUtil.UpdateJson(NewSeasonFormat, "./Data/SeasonsLinks.json")
        SeasonManager.UpdateSeasonLinks()

Exec = UpdateSeasonLinkFormat()
Exec.OverrideFormat()