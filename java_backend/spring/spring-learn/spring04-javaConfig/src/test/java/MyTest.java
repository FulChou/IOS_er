import fulchou_2.Service.UserService;
import fulchou_2.config.Config;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MyTest {
    @Test
    public void test1(){
        ApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
        UserService userService = context.getBean("userService", UserService.class);
        System.out.println(userService.getName());
    }
}
