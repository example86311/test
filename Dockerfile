# 使用 CentOS 作为基础镜像
FROM centos:latest

# 安装必要的软件包
RUN yum -y update && yum -y install vim curl openssh-server vsftpd

# 创建 SSH 配置文件和目录
RUN mkdir -p /var/run/sshd && ssh-keygen -A

# 设置 root 密码
RUN echo 'root:root' | chpasswd

# 配置 vsftpd（FTP）服务
RUN echo "anonymous_enable=NO" >> /etc/vsftpd/vsftpd.conf \
    && echo "local_enable=YES" >> /etc/vsftpd/vsftpd.conf \
    && echo "write_enable=YES" >> /etc/vsftpd/vsftpd.conf \
    && echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf

# 启动 SSH 服务和 FTP 服务
CMD /usr/sbin/sshd -D & /usr/sbin/vsftpd
