<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/wyf7685/wyf7685/main/assets/NoneBotPlugin.svg" width="300" alt="logo">
  </a>
</div>

<div align="center">

# nonebot-plugin-talk-stats

_✨ 群聊活跃度统计 ✨_

[![license](https://img.shields.io/github/license/wyf7685/nonebot-plugin-talk-stats.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-talk-stats?logo=python&logoColor=edb641)](https://pypi.python.org/pypi/nonebot-plugin-talk-stats)
[![python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=edb641)](https://www.python.org/)

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![basedpyright - checked](https://img.shields.io/badge/basedpyright-checked-42b983)](https://docs.basedpyright.com)

[![pre-commit](https://results.pre-commit.ci/badge/github/wyf7685/nonebot-plugin-talk-stats/master.svg)](https://results.pre-commit.ci/latest/github/wyf7685/nonebot-plugin-talk-stats/master)
[![CI](https://github.com/wyf7685/nonebot-plugin-talk-stats/actions/workflows/ci.yml/badge.svg)](https://github.com/wyf7685/nonebot-plugin-talk-stats/actions/workflows/ci.yml)
[![publish](https://github.com/wyf7685/nonebot-plugin-talk-stats/actions/workflows/publish.yml/badge.svg)](https://github.com/wyf7685/nonebot-plugin-talk-stats/actions/workflows/publish.yml)

</div>

## 📖 介绍

基于 [`nonebot-plugin-chatrecorder`](https://github.com/noneplugin/nonebot-plugin-chatrecorder) 数据的群聊活跃度统计插件

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-talk-stats

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

```sh
uv add nonebot-plugin-talk-stats
```

</details>
<details>
<summary>pdm</summary>

```sh
pdm add nonebot-plugin-talk-stats
```

</details>
<details>
<summary>poetry</summary>

```sh
poetry add nonebot-plugin-talk-stats
```

</details>
<details>
<summary>conda</summary>

```sh
conda install nonebot-plugin-talk-stats
```

</details>
<details>
<summary>pip</summary>

```sh
pip install nonebot-plugin-talk-stats
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_talk_stats"]

</details>

> [!note]
> 
> 可选: 启用定时任务功能
> 
> - 将上述 `nonebot-plugin-talk-stats` 改为 `nonebot-plugin-talk-stats[scheduler]` 执行
> 
> - 或手动安装插件 [`nonebot-plugin-apscheduler`](https://github.com/nonebot/plugin-apscheduler)

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|             配置项              | 必填 |     默认值      |         说明         |
| :-----------------------------: | :--: | :-------------: | :------------------: |
| `talk_stats__enable_scheduler`  |  否  |     `True`      | 是否启用定时任务功能 |
| `talk_stats__scene_color_start` |  否  | `(29, 113, 48)` |   群组柱状图渐变色   |
|  `talk_stats__scene_color_end`  |  否  | `(52, 208, 88)` |   群组柱状图渐变色   |
|   `talk_stats__user_color_fn`   |  否  |        -        | 个人统计瓷砖着色函数 |

- `talk_stats__enable_scheduler` 需要安装 `nonebot-plugin-apscheduler`, 未安装时将自动禁用功能
- 渐变色配置项应为 RGB 三元组, 在 `.env.*` 中应写为 `[R, G, B]`
- 着色函数
  - 函数签名应为 `(count: int, total: int) -> str`, 返回形如 `#0f0f0f` 的字符串
  - 在 `.env.*` 中应写为 点分表示法对象 的字符串: `mod.submod:func` [参考](https://github.com/nonebot/nonebot2/blob/v2.4.2/nonebot/utils.py#L285)

## 🎉 使用

[Alconna](https://nonebot.dev/docs/next/best-practice/alconna/matcher) 命令: `talk_stats`

使用示例:

```sh
# 个人水群瓷砖
talk_stats my
talk_stats my --days 120

# 群组活跃度排行
talk_stats scene
talk_stats scene --days 30 --num 10

# 设置定时任务 (需要安装 nonebot-plugin-apscheduler)
talk_stats schedule add 23 59 --num 10
talk_stats schedule clear

# 获取完整命令说明
talk_stats --help
```

## 💡 鸣谢

- [`nonebot/nonebot2`](https://github.com/nonebot/nonebot2): 跨平台 Python 异步机器人框架
- [`noneplugin/nonebot-plugin-chatrecorder`](https://github.com/noneplugin/nonebot-plugin-chatrecorder): 统计数据源
- [`nonebot/plugin-alconna`](https://github.com/nonebot/plugin-alconna): 跨平台的消息处理接口
- [`RF-Tar-Railt/nonebot-plugin-uninfo`](https://github.com/RF-Tar-Railt/nonebot-plugin-uninfo): 绘图信息获取

## 📝 更新日志

<details>
<summary>更新日志</summary>

- 2025.06.09 v0.1.1

  - 插件上传

</details>
