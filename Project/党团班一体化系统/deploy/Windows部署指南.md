# 党团班一体化系统 — Windows Server 部署指南

## 整体架构

```
浏览器 → Nginx (端口80/443) → Waitress (端口8080) → Django WSGI → MySQL
              ↑ 直接返回静态文件
```

| 组件 | 作用 | 安装方式 |
|---|---|---|
| Python 3.12 | 运行 Django 代码 | python.org 下载 |
| Waitress | WSGI 生产服务器(替代 Gunicorn) | pip install |
| Nginx | 反向代理 + 静态文件服务 | nginx.org 下载 |
| MySQL 8.0 | 数据库 | mysql.com 下载 |
| NSSM | 将 Waitress 注册为 Windows 服务 | nssm.cc 下载 |

---

## 第一步：云服务器基础配置

### 1.1 安全组开放端口
登录阿里云控制台 → ECS → 安全组 → 添加入方向规则：
- `80` (HTTP)
- `443` (HTTPS，可选)
- `3306` 只开放给 `127.0.0.1`（MySQL，防外网访问）
- `3389` (远程桌面，你已经在用)

### 1.2 远程桌面连接服务器
用 Windows 自带的"远程桌面连接"连上服务器。

---

## 第二步：安装基础软件

### 2.1 安装 Python 3.12
1. 下载: https://www.python.org/downloads/ → Python 3.12.x Windows Installer (64-bit)
2. **安装时勾选 "Add Python to PATH"**
3. 安装完成后打开 PowerShell 验证：
```powershell
python --version   # 应显示 Python 3.12.x
```

### 2.2 安装 MySQL 8.0
1. 下载: https://dev.mysql.com/downloads/installer/
2. 选择 "Server only" 安装类型
3. 设置 root 密码（记住这个密码）
4. 安装完成后，MySQL 会自动以 Windows 服务运行

### 2.3 安装 Nginx for Windows
1. 下载: https://nginx.org/en/download.html → 选择 Stable version → 下载 zip
2. 解压到 `C:\nginx\`
3. 测试：打开 PowerShell 运行：
```powershell
cd C:\nginx
.\nginx.exe -t   # 测试配置文件语法，应显示 OK
```

### 2.4 下载 NSSM (Non-Sucking Service Manager)
1. 下载: https://nssm.cc/download → nssm-2.24.zip
2. 解压 `nssm.exe` (64位版本) 到 `C:\Windows\System32\` (或 `C:\nginx\`)

---

## 第三步：上传项目代码

### 方式A：直接复制（推荐）
将你本机 `D:\ProjectBase\SystemDesign\` 整个目录打包成 zip，通过远程桌面粘贴到服务器上，保持相同路径：
```
D:\ProjectBase\SystemDesign\Project\党团班一体化系统\
```

### 方式B：Git 拉取
如果代码已上传到 Git 仓库，在服务器上：
```powershell
cd D:\ProjectBase
git clone <你的仓库地址> SystemDesign
```

---

## 第四步：配置项目

### 4.1 创建虚拟环境并安装依赖
在服务器 PowerShell 中：
```powershell
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"
python -m venv venv
.\venv\Scripts\activate

# 安装项目依赖 + 生产服务器
pip install -r requirements.txt
pip install waitress
```

### 4.2 配置生产环境变量
编辑项目根目录的 `.env` 文件（替换成生产值）：
```env
DEBUG=False
SECRET_KEY=换成随机生成的密钥(下面有生成方法)
ALLOWED_HOSTS=你的服务器公网IP,你的域名
CSRF_TRUSTED_ORIGINS=http://你的服务器公网IP

DB_NAME=党团班一体化系统
DB_USER=root
DB_PASSWORD=你安装MySQL时设的密码
DB_HOST=localhost
DB_PORT=3306
```

**生成 SECRET_KEY：**
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4.3 创建数据库并迁移
```powershell
# 先确认 MySQL 服务在运行
Get-Service MySQL80

# 创建数据库 (用 MySQL 命令行)
mysql -u root -p
```
在 MySQL 提示符中：
```sql
CREATE DATABASE IF NOT EXISTS `党团班一体化系统` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
EXIT;
```
回到 PowerShell：
```powershell
# 执行数据库迁移
python manage.py migrate

# 导入种子数据
python manage.py seed_data
```

### 4.4 收集静态文件
```powershell
python manage.py collectstatic --noinput
```
这会把所有静态文件收集到 `staticfiles/` 目录，Nginx 从这里直接返回。

---

## 第五步：配置 Nginx

### 5.1 替换 Nginx 配置
将项目 `deploy/nginx.conf` 复制到 `C:\nginx\conf\nginx.conf`（覆盖原文件）。

**修改 nginx.conf 中的关键内容：**
1. `server_name 你的服务器IP;` → 换成阿里云 ECS 的公网 IP
2. 静态文件路径确认正确：`alias "D:/ProjectBase/SystemDesign/Project/党团班一体化系统/staticfiles/";`

### 5.2 注册 Nginx 为 Windows 服务（开机自启）
以**管理员身份**打开 PowerShell：
```powershell
cd C:\nginx
nssm install nginx C:\nginx\nginx.exe
nssm set nginx AppDirectory C:\nginx
nssm set nginx Start SERVICE_AUTO_START
nssm start nginx
```

---

## 第六步：注册 Django 应用为 Windows 服务

以**管理员身份**打开 PowerShell：
```powershell
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"

# 注册 Waitress 服务
nssm install 党团班一体化 "D:\ProjectBase\SystemDesign\Project\党团班一体化系统\venv\Scripts\python.exe" "D:\ProjectBase\SystemDesign\Project\党团班一体化系统\deploy\waitress_server.py"
nssm set 党团班一体化 AppDirectory "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"
nssm set 党团班一体化 Start SERVICE_AUTO_START
nssm set 党团班一体化 AppStdout "D:\ProjectBase\SystemDesign\Project\党团班一体化系统\deploy\server.log"
nssm set 党团班一体化 AppStderr "D:\ProjectBase\SystemDesign\Project\党团班一体化系统\deploy\server.log"
nssm start 党团班一体化
```

验证服务是否启动成功：
```powershell
nssm status 党团班一体化   # 应显示 SERVICE_RUNNING
Get-Service 党团班一体化     # 应显示 Running
```

---

## 第七步：验证部署

### 7.1 本地测试
在服务器浏览器打开: `http://127.0.0.1`
应看到系统首页。

### 7.2 外网测试
在你自己电脑浏览器打开: `http://<服务器公网IP>`
应看到系统首页。

### 7.3 功能验证
用种子账号登录测试：
- 学号 `20240001` 密码 `123456` (班长)
- 学号 `20240003` 密码 `123456` (学生)
- 学号 `20240002` 密码 `123456` (团支书)

---

## 日常运维

### 查看服务状态
```powershell
Get-Service nginx,党团班一体化 | Format-Table Name,Status,StartType
```

### 重启 Django 应用
```powershell
nssm restart 党团班一体化
```

### 查看日志
```powershell
# Django 应用日志
Get-Content "D:\ProjectBase\SystemDesign\Project\党团班一体化系统\deploy\server.log" -Tail 50

# Nginx 日志
Get-Content C:\nginx\logs\error.log -Tail 30
Get-Content C:\nginx\logs\access.log -Tail 30
```

### 更新代码后
```powershell
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"
.\venv\Scripts\activate
python manage.py migrate          # 执行新迁移
python manage.py collectstatic --noinput  # 收集新静态文件
nssm restart 党团班一体化          # 重启应用
```

### 删除/重装服务
```powershell
nssm stop 党团班一体化
nssm remove 党团班一体化 confirm
```

---

## 可选：配置 HTTPS (SSL证书)

### 阿里云免费 SSL 证书
1. 阿里云控制台 → SSL证书 → 免费证书 → 立即购买 → 申请
2. 填写域名 → DNS验证 → 自动签发
3. 下载 → 选择 "Nginx" → 得到 `.crt` 和 `.key` 文件
4. 放到 `C:\nginx\ssl\` 目录
5. 修改 `nginx.conf`：启用 HTTPS 部分，注释掉 HTTP 部分
6. 重启 Nginx：`nssm restart nginx`
7. 安全组开放 443 端口

---

## 常见问题

### Q: 外网访问不了？
- 检查阿里云安全组是否开放了 80 端口
- 检查 Windows 防火墙: `wf.msc` → 入站规则 → 允许 80,443,8080
- `netstat -ano | findstr :80` 确认 Nginx 正在监听

### Q: 静态文件不显示 (CSS/JS 404)?
- 确认执行了 `python manage.py collectstatic --noinput`
- 确认 nginx.conf 中 static 路径正确定向到 `staticfiles/` 目录

### Q: 服务启动后秒退？
```powershell
# 直接用命令行跑，看具体报错
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"
.\venv\Scripts\python.exe deploy\waitress_server.py
```

### Q: MySQL 连接失败？
- 确认 MySQL 服务在运行: `Get-Service MySQL80`
- 确认 `.env` 中密码正确
- 确认数据库已创建: `mysql -u root -p -e "SHOW DATABASES;"`
