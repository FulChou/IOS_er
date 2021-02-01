import com.fulchou.Service.UserService;
import com.fulchou.Service.UserServiceImp;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test1 {
    @Test
    public void test1(){
        ApplicationContext context =  new ClassPathXmlApplicationContext("ApplicationContext.xml");
        UserService service = context.getBean("userServiceImp", UserServiceImp.class);// 实例名
        System.out.println(service.getName()+" "+ service.getId());
        System.out.println(service.getHoppy());

    }
}
