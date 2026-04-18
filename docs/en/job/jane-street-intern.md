![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# From Top Universities to a Top Quant Firm: Inside the Jane Street Internship Experience

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

This article shares the firsthand experiences of three individuals who interned at Jane Street and successfully converted to full-time roles, offering an inside look at the firm's technology internship program.

Jane Street is a globally renowned quantitative trading firm and liquidity provider, founded in 2000 and headquartered in New York City. With over 2,600 employees worldwide, the firm operates across New York, London, Hong Kong, Amsterdam, Chicago, and Singapore.

As a major market maker, Jane Street trades on over 200 venues globally, spanning equities, bonds, options, futures, commodities, digital assets, and currencies. In 2020, the firm traded over $17 trillion in securities.

Jane Street is distinguished by its technology-driven trading strategies and its extensive use of the OCaml programming language for developing trading systems and tools. The firm emphasizes collaboration and problem-solving, with a strong commitment to innovation in both technology and trading.

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2024/11/26/1732636375053-896444d7-81a0-43ad-b0cb-e89be0aa622a.png)

## The Path to Functional Programming: From Campus to Internship

### Intern A's Story

**Background**: Intern A attended Carnegie Mellon University (CMU), renowned for its programming language research group and rich functional programming curriculum. During her time there, she developed a deep interest in functional programming, actively studying it and even teaching a course called "Hype for Types" to promote functional programming concepts.

**How she discovered the firm**: In class, students often asked, "When is functional programming actually useful in the real world?" The common answer was to mention Jane Street, followed by the caveat: "Don't mention them -- they're the only company using functional programming at scale." This piqued her curiosity.

**Motivation for applying**: Driven by her passion for functional programming, applying felt like a natural decision. She wanted to put her knowledge into practice and work alongside like-minded people.

### Intern B's Story

**Background**: Intern B studied at Harvard, majoring in computer science and statistics. She took a functional programming course and developed an interest in OCaml. During the course, Ron Minsky (a prominent technology leader) gave a talk on real-world applications of OCaml, further sparking her interest.

**How she discovered the firm**: Intern B participated in the INSIGHT program, a week-long camp designed for women in STEM held at the firm's New York office. Participants worked through a series of OCaml exercises and projects, gaining a deep understanding of the firm's technical culture and work environment.

**Motivation for applying**: The INSIGHT program exposed her to the firm's open culture and technical strength. Her interactions with employees convinced her to apply for an internship and pursue deeper involvement in real projects.

### Intern C's Story

**Background**: Intern C attended the University of Cambridge and was introduced to functional programming during his studies. Although OCaml was not as widely taught at his university as at others, this did not diminish his interest.

**How he discovered the firm**: A friend who had interned at Jane Street shared engaging stories about the experience, sparking Intern C's strong interest in the firm.

**Motivation for applying**: Encouraged by his friend's recommendation and his own enthusiasm for functional programming, Intern C decided to apply, hoping to put his knowledge to work in a real-world setting and take on new challenges.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/11/26/1732636409842-603d73f7-fe42-4910-aaff-5dd846a4d84a.png)

## The Internship: Deep Involvement in Core Projects

### Intern A's Experience

**Project Overview**: Intern A worked on improving the firm's manual order entry system, which allows traders to manually submit orders to the market and includes various risk controls.

**Challenges and Solutions**:

- **Problem**: Traders were unable to quickly adjust system-level risk limits during the trading day, which could impact trading efficiency during periods of market volatility. The previous process required configuration file changes, code review, and deployment -- a slow workflow.
- **Her task**: Optimize the system so traders could rapidly adjust system-level risk limits intraday while maintaining compliance and security.
- **Implementation**: She developed a deep understanding of existing risk control mechanisms, worked closely with the team, and designed and built a module enabling rapid risk limit adjustments. She also ensured compatibility with the existing system architecture.
- **Outcome**: Intern A successfully delivered the feature, significantly improving system flexibility. After converting to full-time, her work was widely adopted and praised by the trading desk.

### Intern B's Experience

**Project Overview**: Intern B contributed to the development of the Incr_dom library, the firm's OCaml library for building dynamic web applications.

**Challenges and Solutions**:

- **Problem**: The existing Incr_dom library had two interfaces: one simple but limited in functionality, and another powerful but complex. Users had to choose between ease of use and performance.
- **Her task**: Design and implement a new interface that combined the strengths of both -- maintaining ease of use without sacrificing functionality.
- **Implementation**: She studied the library's architecture in depth and thought carefully about API design principles. She also wrote a PPX (preprocessing extension) to simplify the developer experience. Throughout the process, she collaborated closely with her mentor and iterated on the design.
- **Outcome**: Intern B successfully designed the new interface and improved the library's performance, boosting development efficiency and earning recognition from the team.

### Intern C's Experience

**Project Overview**: Intern C worked on the Request for Quote (RFQ) system. The RFQ system allows clients to request quotes from multiple market makers and select the best price for execution.

**Challenges and Solutions**:

- **Problem**: The risk-checking process for manual requests was not sufficiently automated, creating efficiency and security concerns. Manual requests did not go through the same risk controls as automated requests.
- **His task**: Integrate manual requests with the automated system so they would use a unified risk-checking mechanism, ensuring trade safety.
- **Implementation**: He needed to develop a thorough understanding of the RFQ system architecture and trading workflows, and communicate requirements with both the team and traders. He redesigned the manual request processing pipeline so the system could recognize and apply appropriate risk checks.
- **Outcome**: Intern C successfully automated the risk-checking process for manual requests, improving system security and efficiency while reducing the potential for human error.

![](https://fastly.jsdelivr.net/gh/bucketio/img10@main/2024/11/26/1732636504579-6a7747a9-7dc1-4f96-b0b6-8253287a0e3d.png)

## From Intern to Full-Time: New Challenges and Growth

### Intern A's Transition

- **Returning to her team**: Intern A chose to rejoin her internship team and deepen the work she had started.
- **New responsibilities**: As a full-time employee, she took on longer-term, more open-ended projects such as developing options pricing applications. She needed to consider broader system design and performance optimization challenges.
- **Collaboration and innovation**: She actively collaborated across teams and introduced new technical solutions. For example, she implemented Redis caching in one project, significantly improving system performance and response times.

### Intern B's Transition

- **Team selection**: Intern B joined the team where Intern C had previously interned, taking on the task of advancing the RFQ system project.
- **Deeper collaboration**: She needed to work closely with more traders and teams, understanding the challenges they faced during trading and gathering improvement requirements.
- **Technical growth**: In her new role, Intern B continually expanded her technical capabilities, contributing to complex system design, risk controls, and user interface optimization.

### Intern C's Transition

- **New project challenges**: Intern C joined a new team and began working on the Zeroprot project -- a protocol for efficient communication between different applications, designed to address version compatibility and high-performance communication challenges.
- **Key role**: He was responsible for developing new features, designing the protocol, and integrating it with other systems. He also needed to write tools and libraries to make the protocol accessible to other developers.
- **Technical breakthroughs**: He solved numerous technical challenges including data serialization, version compatibility checking, and efficient network communication, making significant contributions to the firm's communication protocol infrastructure.

## Cross-Team Collaboration: Communication and Shared Success

- **Intern A's experience**: She emphasized the firm's open communication culture. During her projects, she collaborated closely with infrastructure and risk control teams to achieve performance improvements. She also learned new techniques and best practices through cross-team interactions.
- **Intern B's experience**: Daily communication with traders gave her a deep appreciation for the importance of understanding user needs. Through direct interaction, she responded quickly to business requirements and provided efficient technical support. She also contributed to UI improvements that made the system more user-friendly.
- **Intern C's experience**: Working on large-scale projects, Intern C coordinated with multiple teams, aligning different technical approaches and requirements. He believes that successful projects depend on strong teamwork and communication. He also actively participated in internal tech talks, sharing his experience and insights.

## Facing Challenges: Growing Through Practice

- **Technical challenges**: Adapting to entirely new tools and technologies -- OCaml, internal development tools, and complex system architectures -- was a shared challenge. Through study and practice, they progressively acquired the necessary skills.
- **Financial knowledge**: Developing a deep understanding of complex financial concepts, trading workflows, and risk control mechanisms was another significant challenge for those without prior financial backgrounds. They bridged this gap through company training programs, discussions with colleagues, and self-study.
- **Confidence and growth**: Working within high-caliber teams, they needed to continually build confidence and overcome self-doubt. They came to understand that learning and growth are ongoing processes, and they actively sought help and feedback.
- **Support and resources**: The firm provided extensive resources and a supportive environment -- including mentorship programs, training courses, and open communication channels -- enabling them to grow continuously through challenges.
- **Culture**: The open corporate culture and receptiveness to new ideas allowed them to freely express their views and actively participate in decision-making. Their suggestions and ideas were acknowledged and adopted, strengthening their sense of belonging and responsibility.

---

## About LLMQuant

LLMQuant is a cutting-edge community of professionals from the world's leading universities and quantitative finance practitioners, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
