# 后端：FastAPI

## 环境

后端使用 `uv` 管理环境。

首先，安装 `uv`：
```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
然后同步依赖：
```shell
git clone https://github.com/JonathanSilver/mysql_fastapi_vue_sample_project
cd mysql_fastapi_vue_sample_project/backend
uv sync
```

## 数据库

本项目默认使用Sqlite3数据库（会在当前目录生成`sqlite.db`文件），连接字符串在`database.py`文件中配置，表结构（`CREATE TABLE`）会在程序启动时自动创建。

## 启动

启动：
```shell
uv run uvicorn main:app
```

文档页面：`http://127.0.0.1:8000/docs`
