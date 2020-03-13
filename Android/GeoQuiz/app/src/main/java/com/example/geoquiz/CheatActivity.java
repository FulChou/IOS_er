package com.example.geoquiz;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewAnimationUtils;
import android.widget.Button;
import android.widget.TextView;

public class CheatActivity extends AppCompatActivity {
    private static final String EXTRA_ANSWER_IS_TRUE =
            "MainActivity.geoquiz.answer_is_true";

    private static final String EXTRA_ANSWER_SHOWN =
            "geoquiz.answer_shown";

    private boolean mAnswerIsTrue;

    private TextView mAnswerTextView;
    private Button mShowAnswer;
    private TextView mSDKTextView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cheat);

        mAnswerTextView = (TextView)findViewById(R.id.answerTextView);
        mShowAnswer = (Button)findViewById(R.id.showAnswerButton);
        mSDKTextView = (TextView)findViewById(R.id.sdk_version);

        mSDKTextView.setText("API level"+Build.VERSION.SDK_INT);


        mAnswerIsTrue = getIntent().getBooleanExtra(EXTRA_ANSWER_IS_TRUE,false);

        mShowAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(mAnswerIsTrue){
                    mAnswerTextView.setText(R.string.true_button);
                }else {
                    mAnswerTextView.setText("这个题目的答案是错的");
                }
                setAnswerShownResult(true);

                if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP){
                    mShowAnswer.setVisibility(View.INVISIBLE);
                }else {
                    // api 21中的函数，29不能使用
//                    int cx = mShowAnswer.getWidth() / 2;
//                    int cy = mShowAnswer.getHeight() / 2;
//                    float radius = mShowAnswer.getWidth();
//                    Animator anim = ViewAnimationUtils
//                            .createCircularReveal(mShowAnswer, cx, cy, radius, 0);
//                    anim.addListener(new AnimatorListenerAdapter() {
//                        @Override
//                        public void onAnimationEnd(Animator animation) {
//                            super.onAnimationEnd(animation);
//                            mShowAnswer.setVisibility(View.INVISIBLE);
//                        }
//                    });
//                    anim.start();
                }

            }
        });

    }

    private void setAnswerShownResult(boolean isAnswerShown) {
        Intent data = new Intent();
        data.putExtra(EXTRA_ANSWER_SHOWN, isAnswerShown);
        setResult(RESULT_OK, data);
    }
}
