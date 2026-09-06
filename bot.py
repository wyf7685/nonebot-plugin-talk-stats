import nonebot
from nonebot.adapters.milky import Adapter as MilkyAdapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(MilkyAdapter)
nonebot.load_plugin("nonebot_plugin_talk_stats")

if __name__ == "__main__":
    nonebot.run()
