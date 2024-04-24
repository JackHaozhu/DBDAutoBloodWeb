import cv2
import DBDAutoBloodWeb
import time

time.sleep(1)
target_list = (cv2.imread(r"D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Items\iconItems_flashlight.png"),
               cv2.imread(r"D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Items\iconItems_medkit.png"),
               cv2.imread(r"D:\SteamLibrary\steamapps\common\Dead by Daylight\DeadByDaylight\Content\UI\Icons\Items\iconItems_toolbox.png"))
# cv2.imshow("Targets", cv2.hconcat([target_list[0], target_list[1], target_list[2]]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

DBDAutoBloodWeb.click_target(target_list)