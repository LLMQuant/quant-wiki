# Quant-Wiki

<img width="848" alt="image" src="https://github.com/user-attachments/assets/2d3c898d-ad1b-49ac-a7c2-19d2d737fed4" />


> [!NOTE]
> 本项目正在开发中，欢迎大家参与贡献。

the wikipedia for quantitative research.

## **Content**

> [!IMPORTANT]
> 等待内容完善中...

## Contribution

如果您希望为 quant-wiki 做贡献，你需要做的是：

- fork 这个 repo。
- 在 `docs` 文件夹中增添对应的文件/文件夹。
- 在 `mkdocs.yml` 中的 `nav` 字段下进行更新。
- 提交 Pull Request 即可。

## Local Deploy

首先拉取代码，然后进入项目目录。

```bash
git clone https://github.com/LLMQuant/quant-wiki.git
cd quant-wiki
```

推荐使用 `venv` 创建虚拟环境，并安装依赖。

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

本地预览只需要运行如下命令即可：

```bash
mkdocs serve
```
