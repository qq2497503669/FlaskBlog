import os
class Config:
    # 设置环境变量
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you will never guess'
