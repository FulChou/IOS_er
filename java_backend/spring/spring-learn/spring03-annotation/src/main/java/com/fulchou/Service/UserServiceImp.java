package com.fulchou.Service;

import com.fulchou.Dao.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImp implements UserService{
    @Autowired
    User user;

    @Override
    public String getName() {
        return user.getName();
    }

    @Override
    public int getId() {
        return user.getId();
    }

    @Override
    public List<String> getHoppy() {
        return user.getHoppy();
    }
}
