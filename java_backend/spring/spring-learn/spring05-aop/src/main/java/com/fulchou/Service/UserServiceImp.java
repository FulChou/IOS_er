package com.fulchou.Service;

public class UserServiceImp implements UserService{

    @Override
    public void add() {
        System.out.println("添加了一个用户");
    }

    @Override
    public void delete() {
        System.out.println("删除了一个用户");
    }

    @Override
    public void select() {
        System.out.println("选择了一个用户");
    }

    @Override
    public void update() {
        System.out.println("更新了一个用户");
    }
}
