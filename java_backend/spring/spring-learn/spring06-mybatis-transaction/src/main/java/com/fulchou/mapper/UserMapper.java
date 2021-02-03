package com.fulchou.mapper;

import com.fulchou.bean.User;

import java.util.List;

public interface UserMapper {
    public void addUser(User user);
    public User selectUser(int id);
    public void deleteUser(int id);
    public List<User> getUsers();

}
