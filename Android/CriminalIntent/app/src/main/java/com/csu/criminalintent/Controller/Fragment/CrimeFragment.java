package com.csu.criminalintent.Controller.Fragment;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;

import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.csu.criminalintent.Controller.ActivityReqCodeEnum;
import com.csu.criminalintent.Controller.CrimeActivity;
import com.csu.criminalintent.R;
import com.csu.criminalintent.model.Crime;
import com.csu.criminalintent.model.CrimeLab;

import java.util.Date;
import java.util.UUID;

import static android.text.format.DateFormat.format;

public class CrimeFragment extends Fragment {

    private static final String TAG = "Crime ";
    private static final String ARG_CRIME_ID = "crime_id";
    private static final int REQUEST_CRIME = 1;
    private Crime mCrime;
    private EditText mTitleField;
    private Button mDateButton;
    private CheckBox mSolvedCheckBox;
    private Button mTimeButtion;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
// 获得 intent：
//        Intent intent = getActivity().getIntent();
//        UUID crimeId = (UUID)intent.getSerializableExtra(CrimeActivity.EXTRA_CRIME_ID);
//        Log.d(TAG, "onCreate: uuid is "+crimeId);

        UUID crimeId = (UUID)getArguments().getSerializable(ARG_CRIME_ID);
        mCrime = CrimeLab.get(getActivity()).getCrime(crimeId);

    }

    // 初始化
    public static CrimeFragment newInstance(UUID crimeId) {
        Bundle args = new Bundle();
        args.putSerializable(ARG_CRIME_ID, crimeId);
        CrimeFragment fragment = new CrimeFragment();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != Activity.RESULT_OK) {
            return;
        }

        if(requestCode==ActivityReqCodeEnum.DataPickerFragmentResCode.ordinal()){
            // 前后的 key要一致，不然程序竟然会崩溃
            Date date = (Date)data.getSerializableExtra("EXTRA_DATE");

            Log.d("debuging", "onActivityResult: get data:"+date);

            mCrime.setDate(date);
            updateDate();
        }
    }

    private void updateDate() {
        String date = (String) DateFormat.format("EEEE, MMMM dd, yyyy", mCrime.getDate());
        mDateButton.setText(date);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.fragment_crime, container, false);

        mTitleField = (EditText)v.findViewById(R.id.crime_title);
        mTitleField.setText(mCrime.getTitle());

        mTitleField.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(
                    CharSequence s, int start, int count, int after) {
                // This space intentionally left blank
            }

            @Override
            public void onTextChanged(
                    CharSequence s, int start, int before, int count) {
                mCrime.setTitle(s.toString());
                // page 返回传值函数
                //returnResult();
                System.out.println(mCrime.getTitle());
            }

            @Override
            public void afterTextChanged(Editable editable) {
                // must implement
            }
        });

        mDateButton = (Button)v.findViewById(R.id.crime_date);
        // 进行时间的格式转化：
        String date = (String) DateFormat.format("EEEE, MMMM dd, yyyy", mCrime.getDate());
        updateDate();
        //mDateButton.setEnabled(false);
        mDateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FragmentManager manager = getFragmentManager();
                DatePickerFragment dialogFragment =  DatePickerFragment.newInstance(mCrime.getDate());
                dialogFragment.setTargetFragment(CrimeFragment.this, ActivityReqCodeEnum.DataPickerFragmentResCode.ordinal());
                dialogFragment.show(manager, "DIALOG_DATE");
            }
        });

        mTimeButtion = (Button) v.findViewById(R.id.crime_time);
        mTimeButtion.setText("please input time crime");
        mTimeButtion.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                FragmentManager manager = getFragmentManager();

                TimePickerFragment dialogTimeFragment =  TimePickerFragment.newInstance();

                dialogTimeFragment.setTargetFragment(CrimeFragment.this, ActivityReqCodeEnum.TimePickerFragmentResCode.ordinal());
                dialogTimeFragment.show(manager, "DIALOG_TIME");

        }
        });



        mSolvedCheckBox = (CheckBox) v.findViewById(R.id.crime_solved);
        mSolvedCheckBox.setChecked(mCrime.isSolved());
        // click event
        mSolvedCheckBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                mCrime.setSolved(b);

            }
        });


        return v;
    }



    public void returnResult(int index){
        Intent data = new Intent();
        data.putExtra("currentCrimeIndex",index);
        getActivity().setResult(CrimeActivity.RESULT_OK, data);
    }


}
