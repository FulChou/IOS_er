package com.csu.criminalintent.Controller.Fragment;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.csu.criminalintent.Controller.ActivityReqCodeEnum;
import com.csu.criminalintent.Controller.CrimeActivity;
import com.csu.criminalintent.Controller.CrimePagerActivity;
import com.csu.criminalintent.R;
import com.csu.criminalintent.model.Crime;
import com.csu.criminalintent.model.CrimeLab;

import java.util.List;

import static android.content.ContentValues.TAG;

public class CrimeListFragment extends Fragment {
    private RecyclerView mCrimeRecyclerView;

    private CrimeAdapter mAdapter;
    private int mCurrentClickIndex ;



    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_crime_list, container, false);

        mCrimeRecyclerView = (RecyclerView) v.findViewById(R.id.crime_recycler_view);
        mCrimeRecyclerView.setLayoutManager(new LinearLayoutManager(getActivity())); // what mean
        //System.out.println("test ");
        updateUI();
        return v;
    }

    private void updateUI() {
        CrimeLab crimeLab = CrimeLab.get(getActivity());
        List<Crime> crimes = crimeLab.getCrimes();

        if (mAdapter == null) {
            mAdapter = new CrimeAdapter(crimes);
            mCrimeRecyclerView.setAdapter(mAdapter);
        } else {
            // not null refrash
//            mAdapter.notifyDataSetChanged();
            mAdapter.notifyItemChanged(mCurrentClickIndex);
        }


    }

    // 在展示之前调用刷新视图
    @Override
    public void onResume() {
        super.onResume();
        updateUI();
    }


    // 接受返回调用的值：
    public void onActivityResult(int requestCode, int resultCode, Intent data) {

        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != Activity.RESULT_OK) {
            return;
        }
        if (requestCode == ActivityReqCodeEnum.CrimeActivityRequestCode.ordinal()) {
            if (data == null) {
                return;
            }
            String testString = data.getStringExtra("test");
            Log.d("debuging", "onActivityResult: "+testString);
        }
    }

    // viewHOlder:
    private class CrimeHolder extends RecyclerView.ViewHolder {
//        public TextView mTitleTextView;

        private TextView mTitleTextView;
        private TextView mDateTextView;
        private CheckBox mSolvedCheckBox;
        private Crime mCrime;

        public CrimeHolder(View itemView) {
            super(itemView);
            // 定义点击 event
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    //Intent intent = new Intent(getActivity(), CrimeActivity.class);
//                    Intent intent = CrimeActivity.newIntent(getActivity(),mCrime.getId());
                    Intent intent = CrimePagerActivity.newIntent(getActivity(), mCrime.getId());
                    //startActivityForResult(intent, ActivityReqCodeEnum.CrimeActivityRequestCode.ordinal());

                    mCurrentClickIndex = mCrimeRecyclerView.getChildAdapterPosition(view);

                    startActivity(intent);

                   // Toast.makeText(getActivity(),mCrime.getTitle()+"Clicked!",Toast.LENGTH_SHORT).show();
//                    mCrimeRecyclerView.getAdapter().notifyItemMoved(0, 5);
//                    Log.d(TAG, "onClick: sfdf");
                }
            });

//            mTitleTextView = (TextView) itemView;
            mTitleTextView = (TextView)itemView.findViewById(R.id.list_item_titleText);
            mDateTextView = (TextView)itemView.findViewById(R.id.list_item_data_textView);
            mSolvedCheckBox = (CheckBox)itemView.findViewById(R.id.list_item_checkBox);


        }

        public void bindCrime(Crime crime) {
            mCrime = crime;
            mTitleTextView.setText(mCrime.getTitle());
            mDateTextView.setText(mCrime.getDate().toString());
            mSolvedCheckBox.setChecked(mCrime.isSolved());

//            mSolvedCheckBox.setOnClickListener(new CompoundButton.OnCheckedChangeListener(){
//                @Override
//                public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
//
//                }
//            });
        }


    }

    // Adapter:
    private class CrimeAdapter extends RecyclerView.Adapter<CrimeHolder>{
        private List<Crime> mCrimes;
        private  Crime crrentCrime;

        public  CrimeAdapter(List<Crime>crimes){
            mCrimes = crimes;
        }

        @NonNull
        @Override
        public CrimeHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            //需要新的View视图来显示列表项时，会调用onCreateViewHolder方法
            LayoutInflater layoutInflater = LayoutInflater.from(getActivity());
            // 系统的样式 ： View view = layoutInflater.inflate(android.R.layout.simple_list_item_1,parent,false);// what mean?
            View view = layoutInflater.inflate(R.layout.list_item_crime,parent,false);
            return new CrimeHolder(view);
        }

        @Override
        public void onBindViewHolder(@NonNull CrimeHolder holder, int position) {
             crrentCrime = mCrimes.get(position);
//            holder.mTitleTextView.setText(crime.getTitle());

//            holder.mSolvedCheckBox.setOnClickListener(new CompoundButton.OnCheckedChangeListener() {
//                @Override
//                public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
//                    crrentCrime.setSolved(b);
//                }
//            });

            holder.bindCrime(crrentCrime);


        }

        @Override
        public int getItemCount() {
            return mCrimes.size();
        }
    }
}
