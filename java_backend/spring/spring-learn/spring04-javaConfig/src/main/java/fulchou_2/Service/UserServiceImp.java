package fulchou_2.Service;

import fulchou_2.Dao.User;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class UserServiceImp implements UserService{
    @Autowired
    User user;

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

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
