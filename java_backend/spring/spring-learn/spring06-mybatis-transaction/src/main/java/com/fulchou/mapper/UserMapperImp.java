package com.fulchou.mapper;

import com.fulchou.bean.User;
import org.mybatis.spring.support.SqlSessionDaoSupport;

import java.util.List;

public class UserMapperImp extends SqlSessionDaoSupport implements UserMapper{
    @Override
    public void addUser(User user) {
    getSqlSession().getMapper(UserMapper.class).addUser(user);
    }

    @Override
    public User selectUser(int id) {
        return null;
    }

    @Override
    public void deleteUser(int id) {
        getSqlSession().getMapper(UserMapper.class).deleteUser(id);

    }

    @Override
    public List<User> getUsers() {
        UserMapper mapper = getSqlSession().getMapper(UserMapper.class);
        User user = new User("lklll",3,"zhoufu ");
        mapper.addUser(user);

        mapper.deleteUser(3);
        return mapper.getUsers();
    }
}
