# 如何参与  

在文章开始之前，Quant-Wiki 项目组全体成员十分欢迎您为本项目贡献页面。正因为有了上百位像您一样的人，才有了 Quant-Wiki 的今天！  

这篇文章将主要叙述参与 Quant-Wiki 编写的写作过程。请您在撰稿或者修正 Wiki 页面以前，仔细阅读以下内容，以帮助您完成更高质量的内容。

---

## 贡献指南  

请您在编辑前查看 [Quant-Wiki 贡献指南](https://github.com/LLMQuant/quant-wiki/blob/master/.github/CONTRIBUTING.md) 和项目方针，以更好地和社区贡献者进行合作、交流。

---

## 参与协作  

???+ warning
    在开始编写一段内容之前，请查阅 [Issues](https://github.com/LLMQuant/Quant-Wiki/issues)，确认没有别人在做相同的工作之后，开一个新 Issue 记录待编写的内容。  

???+ tip
    在 Issues 中也有很多待修复/解决的问题，尤其是我们的迭代计划（Iteration Plan）。从这里获取任务是一个很好的开始！

为了保证条目内容的专业性和准确性，我们建议您在编辑前先考虑以下几点：  

1. **选择您熟悉的领域**：请优先编辑那些与您的专业知识、学习背景或兴趣爱好相关的条目。这有助于您创作出高质量的内容。  
2. **谨慎对待新领域**：如果您对某个主题还处于初学阶段或不太了解，建议您先通过阅读、学习加深理解，待有一定把握后再动手编辑。  
3. **查阅相关资料**：为条目添加内容或进行修订时，建议您先查阅权威文献和资料，确保信息准确无误。也欢迎您在页面评论区或我们的社区提出问题，与其他编者交流讨论。  

我们珍惜每位贡献者的热情和付出，也理解大家的专业水平不尽相同。让我们携手合作，共同呵护这个知识的乐园，用准确、专业的内容去帮助更多读者。期待您的贡献！  

---

## 在 GitHub 上编辑  

参与 Quant-Wiki 的编写需要一个 GitHub 账号（可以前往 [GitHub 注册页面](https://github.com/join) 注册账号），但不需要高超的 GitHub 技巧，即使你是一名新手，只要按照下面所述的步骤操作，也能够非常出色地完成编辑。

???+ tip
    在你的更改被合并到 Quant-Wiki 的主仓库之前，你对 Quant-Wiki 的内容所作出的修改均不会出现在主站上，所以无需担心你的修改会破坏已有的内容。如果还是不放心，可以参考 [GitHub 官方教程](https://docs.github.com/cn/get-started/quickstart/contributing-to-projects)。

---

### 编辑单个页面的内容  

1. 在 Quant-Wiki 项目中找到对应页面；  
2. 点击正文右上方的 **「编辑此页」（edit）** 按钮，根据提示跳转到 GitHub 进行编辑；  
3. 在编辑框内编写或修改内容，请关闭自动翻译工具，避免因翻译问题导致错误；  
4. 编写完成后，滚动到页面下方，按照 [commit 信息格式规范](#commit-信息格式规范) 填写 commit 信息，然后点击 **Propose changes** 按钮提交修改；  
5. 点击页面上方的绿色 **Create pull request** 按钮，根据提示完成 PR 提交；  
6. PR 提交后，等待管理员审核并合并即可。  

---

### 编辑多个页面的内容  

如果需要编辑多个页面，可以使用 GitHub 的 Web 编辑器：  

1. 打开 Quant-Wiki 仓库，按下 `.` 键进入网页版 VS Code；  
2. 在编辑器中对源文件进行更改，完成后提交修改；  
3. 提交时创建分支并按照 [commit 信息格式规范](#commit-信息格式规范) 填写信息；  
4. 创建 Pull Request 并等待审核。

---

### 使用 Git 在本地进行编辑  

对于更复杂的改动，可以在本地使用 Git 进行编辑：  

1. Fork 仓库并克隆到本地；  
2. 在本地进行修改后提交（commit）更改；  
3. 推送（push）更改到远程仓库；  
4. 提交 Pull Request 至主仓库。

详细流程请参考 [Git 文档](https://git-scm.com/doc)。

---

## Commit 信息格式规范  

在提交更改时，请遵守以下规范：  

1. Commit 摘要简要描述改动内容，长度不超过 50 字符；  
2. 可在正文中详细描述本次修改；  
3. 推荐格式：  

   ```
   <修改类型>(<文件名>): <修改的内容>
   ```  

   修改类型包括：  
   - **feat**：用于添加内容；  
   - **fix**：用于修正内容错误；  
   - **refactor**：用于重构页面内容；  
   - **revert**：用于回退更改。

---

## Pull Request 信息格式规范  

提交 Pull Request 时，请注意以下几点：  

1. 标题清晰表述改动内容，例如：  

   ```
   fix(math/poly/fft): 修正公式错误 (#123)
   feat(ds/segment-tree): 添加更多示例 (#456)
   ```  

2. 在内容中标明改动详情，如果修复了 Issue，请在正文中添加 `fix #编号` 字段；  
3. 确认 PR 符合 [贡献指南](https://github.com/LLMQuant/quant-wiki/blob/master/.github/CONTRIBUTING.md) 后提交。

---

## 协作流程  

1. 提交 PR 后，等待 GitHub Actions 和 Netlify 测试完成；  
2. Reviewer 可能会提出修改建议，您可以根据需要追加更改；  
3. 通过足够多的 Reviewer 审核后，PR 会被合并到主分支；  
4. 主分支更新后，网站内容将自动重新构建并部署。

---

感谢您的热情参与！如果您有任何问题，可以在 [GitHub Issues](https://github.com/LLMQuant/Quant-Wiki/issues) 中提出。我们期待您的贡献！

---

## 参考资料与注释  

1. [维基百科：新手入门/编辑](https://zh.wikipedia.org/wiki/Wikipedia:新手入门/编辑) ↩  
2. [Web-based editor - GitHub Codespaces - GitHub Docs](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) ↩  
