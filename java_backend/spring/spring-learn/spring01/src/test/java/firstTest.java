import com.csu.dao.UserDao;
import com.csu.dao.UserDaoImp;
import com.csu.dao.UserDaoMysqlImp;
import com.csu.service.UserService;
import com.csu.service.UserServiceImp;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class firstTest {
    public static void main(String[] args) {
//        UserService userService = new UserServiceImp();
//
//        UserDao userDao = new UserDaoMysqlImp();
//        //  手动，依赖注入：
//        ((UserServiceImp) userService).setUserDao(userDao);
//        userService.getUser();
        // 配置文件配置， 注入对象：：
        ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
        UserService userService = (UserService) context.getBean("userService");
        userService.getUser();
        System.out.println();
    }
}
