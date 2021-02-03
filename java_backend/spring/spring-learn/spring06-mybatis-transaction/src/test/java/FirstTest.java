import com.fulchou.mapper.UserMapperImp;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class FirstTest {
    @Test
    public  void test1(){
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        UserMapperImp userMapper = context.getBean("userMapper", UserMapperImp.class);
        System.out.println(userMapper.getUsers());

    }
}
