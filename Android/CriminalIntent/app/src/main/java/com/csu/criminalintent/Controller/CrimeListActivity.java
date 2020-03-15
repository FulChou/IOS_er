package com.csu.criminalintent.Controller;

import androidx.fragment.app.Fragment;

import com.csu.criminalintent.Controller.Fragment.CrimeListFragment;

public class CrimeListActivity extends SingleFragmentActivity {
    @Override
    protected Fragment createFragment() {
        return new CrimeListFragment();
    }
}
