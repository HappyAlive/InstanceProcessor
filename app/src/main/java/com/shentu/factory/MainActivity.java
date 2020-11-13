package com.shentu.factory;

import android.os.Bundle;
import android.util.Log;

import com.shentu.factory.ui.main.MainFragment;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
        if (savedInstanceState == null) {
            getSupportFragmentManager().beginTransaction()
                    .replace(R.id.container, MainFragment.newInstance())
                    .commitNow();
        }
//        .create()

//        InstanceFactory.create()
        Log.d("long class",long.class.getSimpleName());
    }
}