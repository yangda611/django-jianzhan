#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
清除Django缓存的脚本
"""
import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sx_cms.settings')
django.setup()

from django.core.cache import cache
from django.core.management import execute_from_command_line

def clear_all_cache():
    """清除所有缓存"""
    print("正在清除Django缓存...")
    
    try:
        # 清除Django缓存
        cache.clear()
        print("✅ Django缓存已清除")
        
        # 清除数据库缓存表
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM my_cache_table")
            print("✅ 数据库缓存表已清空")
        
        print("🎉 所有缓存清除完成！")
        
    except Exception as e:
        print(f"❌ 清除缓存时出错: {e}")

def check_cache_status():
    """检查缓存状态"""
    print("\n检查缓存状态...")
    
    try:
        # 检查缓存表是否存在
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES LIKE 'my_cache_table'")
            result = cursor.fetchone()
            
            if result:
                cursor.execute("SELECT COUNT(*) FROM my_cache_table")
                count = cursor.fetchone()[0]
                print(f"📊 缓存表记录数: {count}")
            else:
                print("⚠️  缓存表不存在")
        
        # 测试缓存
        cache.set('test_key', 'test_value', 60)
        test_value = cache.get('test_key')
        if test_value == 'test_value':
            print("✅ 缓存功能正常")
        else:
            print("❌ 缓存功能异常")
            
    except Exception as e:
        print(f"❌ 检查缓存状态时出错: {e}")

if __name__ == '__main__':
    print("=" * 50)
    print("Django缓存清除工具")
    print("=" * 50)
    
    clear_all_cache()
    check_cache_status()
    
    print("\n" + "=" * 50)
    print("建议：清除缓存后请重启Django服务器")
    print("=" * 50)
