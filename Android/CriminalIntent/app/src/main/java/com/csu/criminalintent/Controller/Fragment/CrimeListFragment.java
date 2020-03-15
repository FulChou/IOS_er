package com.csu.criminalintent.Controller.Fragment;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.csu.criminalintent.R;
import com.csu.criminalintent.model.Crime;
import com.csu.criminalintent.model.CrimeLab;

import java.util.List;

import static android.content.ContentValues.TAG;

public class CrimeListFragment extends Fragment {
    private RecyclerView mCrimeRecyclerView;

    private CrimeAdapter mAdapter;



    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        System.out.println("----------");

    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_crime_list, container, false);
        mCrimeRecyclerView = (RecyclerView) v.findViewById(R.id.crime_recycler_view);
        mCrimeRecyclerView.setLayoutManager(new LinearLayoutManager(getActivity())); // what mean
        System.out.println("test ");
        setupUI();
        return v;
    }

    private void setupUI() {
        CrimeLab crimeLab = CrimeLab.get(getActivity());
        List<Crime> crimes = crimeLab.getCrimes();
        mAdapter = new CrimeAdapter(crimes);

        mCrimeRecyclerView.setAdapter(mAdapter);


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
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Toast.makeText(getActivity(),mCrime.getTitle()+"Clicked!",Toast.LENGTH_SHORT).show();
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
        }


    }

    // Adapter:
    private class CrimeAdapter extends RecyclerView.Adapter<CrimeHolder>{
        private List<Crime> mCrimes;
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
            Crime crime = mCrimes.get(position);
//            holder.mTitleTextView.setText(crime.getTitle());
            holder.bindCrime(crime);


        }

        @Override
        public int getItemCount() {
            return mCrimes.size();
        }
    }
}
