#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django缓存管理命令
使用方法: python manage_cache.py [clear|status|disable|enable]
"""
import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sx_cms.settings')
django.setup()

from django.core.cache import cache
from django.db import connection

def clear_cache():
    """清除缓存"""
    print("🧹 正在清除缓存...")
    try:
        cache.clear()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM my_cache_table")
        print("✅ 缓存清除成功")
    except Exception as e:
        print(f"❌ 清除缓存失败: {e}")

def check_status():
    """检查缓存状态"""
    print("📊 检查缓存状态...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM my_cache_table")
            count = cursor.fetchone()[0]
            print(f"缓存表记录数: {count}")
        
        # 测试缓存
        cache.set('test', 'value', 60)
        result = cache.get('test')
        print(f"缓存测试: {'✅ 正常' if result == 'value' else '❌ 异常'}")
    except Exception as e:
        print(f"❌ 检查状态失败: {e}")

def disable_cache():
    """临时禁用缓存"""
    print("🚫 临时禁用缓存...")
    # 这里可以修改settings.py中的CACHES配置
    print("请在settings.py中将CACHES改为DummyCache")

def main():
    if len(sys.argv) < 2:
        print("使用方法: python manage_cache.py [clear|status|disable]")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'clear':
        clear_cache()
    elif command == 'status':
        check_status()
    elif command == 'disable':
        disable_cache()
    else:
        print("未知命令，支持的命令: clear, status, disable")

if __name__ == '__main__':
    main()
