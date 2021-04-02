# Logitech Options 在 Mac 下的自定义按键失灵问题

鼠标：Master 2S

电脑：Mac pro 2018

系统：big sur 11.1

问题描述：电脑睡眠之后，鼠标的自定义功能不能够使用，只能够使用左键，右键

## 排查问题：

1. 修改Security & Privacy 里的 Logi Options Daemon 和 Logi Options 权限，发现已经勾选了
2. 重新安装Logitech Options勾选权限，仍然无法使用

## 解决办法：

1. 在Security & Privacy 中，删除 Logi Options Daemon 和 Logi Options 权限，然后再添加
2. 更新mac os的系统

