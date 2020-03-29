# android 核心编程第二部分

## 第十一章 ViewPager

-  创建一个activity 继承自 FragmentActivity
-  设置contentView（ViewPager）androidx包里面也有
-  PagerAdapter
   -  两个简化试用版：
   -  FragmentStatePagerAdapter
   -  FragmentPagerAdapter 适合pager比较少，占用内存较少的情况。FragmentPagerAdapter只是销毁了fragment的视图，fragment实例还保留在FragmentManager中。因此，FragmentPagerAdapter创建的fragment永远不会被销毁
- setOffscreenPageLimit(int)方法，定制预加载相邻页面的数目。
- mViewPager.setCurrentItem(i); 设置目前打开那个position 的fragment

```java
 FragmentManager fragmentManager = getSupportFragmentManager();
// set adapter
        mViewPager.setAdapter(new FragmentStatePagerAdapter(fragmentManager) {
            @NonNull
            @Override
            public Fragment getItem(int position) {
                Crime crime = mCrimes.get(position);

                return CrimeFragment.newInstance(crime.getId());
            }

            @Override
            public int getCount() {
                return  mCrimes.size();
            }
        });
```

- 以代码的方式创建布局：
  - 以代码的方式创建视图很简单：调用视图类的构造方法，并传入Context参数。不创建任何布局文件，用代码就能创建完整的视图层级机构。



## 第23章 使用 AsyncTask 在后台线程上运行代码

- 如果使用 在AndroidMainfest中添加，在app中进行了网络访问，那么要记得模拟器 uninstall app 并且Androidminst文件中添加：` <uses-permission android:name="android.permission.INTERNET" />`