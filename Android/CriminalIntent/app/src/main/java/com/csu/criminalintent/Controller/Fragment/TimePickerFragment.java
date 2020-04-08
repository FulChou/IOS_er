package com.csu.criminalintent.Controller.Fragment;

import android.app.Activity;
import android.app.Dialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TimePicker;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatDialogFragment;

import com.csu.criminalintent.R;

import java.util.Date;
import java.util.GregorianCalendar;

public class TimePickerFragment extends AppCompatDialogFragment {
    private TimePicker mTimerPicker;
    @NonNull
    @Override
    public Dialog onCreateDialog(@Nullable Bundle savedInstanceState) {

        View v = LayoutInflater.from(getActivity())
                .inflate(R.layout.dialog_time, null);
        mTimerPicker = (TimePicker)v.findViewById(R.id.dialog_data_time_picker);

        return new AlertDialog.Builder(getActivity())
                .setView(v)
                .setTitle("时间选择")
                .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
//                        int year = mDatePicker.getYear();
//                        int month = mDatePicker.getMonth();
//                        int day = mDatePicker.getDayOfMonth();
//                        Date date = new GregorianCalendar(year, month, day).getTime();
//                        Log.d("debuging", "onClick: the ok");
//                        sendResult(Activity.RESULT_OK, date);
                    }
                })
                .create();
    }

    public static TimePickerFragment newInstance() {
        
        Bundle args = new Bundle();
        
        TimePickerFragment fragment = new TimePickerFragment();
        fragment.setArguments(args);
        return fragment;
    }
}
