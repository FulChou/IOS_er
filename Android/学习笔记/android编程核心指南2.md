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

## 第12章 对 话 框

- 使用AppCompat兼容库，添加到依赖中
- 创建 DialogFragment，重写方法onCreateDialog（）返回一个dialog，创建一个布局文件，布局文件的view（包含了一个DatePicker）传递到dialog里面去。


```java
  return new AlertDialog.Builder(getActivity())
                .setView(v)
                .setTitle(R.string.date_picker_title)
                .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        int year = mDatePicker.getYear();
                        int month = mDatePicker.getMonth();
                        int day = mDatePicker.getDayOfMonth();
                        Date date = new GregorianCalendar(year, month, day).getTime();
                        Log.d("debuging", "onClick: the ok");
                        sendResult(Activity.RESULT_OK, date);
                    }
                })
                .create();
```

- 一个fragment，调用一个新的fragment，并且给新的fragment设置返回的目标fragment和req code 

```java
  FragmentManager manager = getFragmentManager();
    DatePickerFragment dialogFragment =  DatePickerFragment.newInstance(mCrime.getDate());
   
    dialogFragment.setTargetFragment(CrimeFragment.this, ActivityReqCodeEnum.DataPickerFragmentResCode.ordinal());
    
    dialogFragment.show(manager, "DIALOG_DATE");
```

- fragment 之间的正向传值：
  - 给子fragment封装一个new instance的方法。其中参数进行参数传值，并且直接把参数放到Bundle对象中去，然后设置fragment的args。
  - 子fragment实例化的时候，自己根据key取args中的值。


- fragment 之间的反向传值：
  - 调用新的fragment，设置res code
  - 在on ActivityResult（）中找到res code 对应的值
  - 子fragment 生成一个intent，然后调用getTargetFragment（），给onActivityresult()传入 result code ，intent。
- 注意：两个fragment 放的intent里面的key 和取的时候用的key要一样。不然就取不到值了。


## 第23章 使用 AsyncTask 在后台线程上运行代码

- 如果使用 在AndroidMainfest中添加，在app中进行了网络访问，那么要记得模拟器 uninstall app 并且Androidminst文件中添加：` <uses-permission android:name="android.permission.INTERNET" />`