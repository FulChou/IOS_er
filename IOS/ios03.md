# lebus教程03

## p58-66:Todos app

- p58 新建一个todos项目
- 将项目添加 tableViewController，并且设置为起始页面，添加对应的类
- 将项目分割成mvc模式，查看tabelviewController的方法
- p58: cell指定一个类，通过方法生成指定identifile 的cell
-   `let cell = tableView.dequeueReusableCell(withIdentifier: "todo", for: indexPath) as! TodosCell`//重用cell
- 然后给cell里面加label控件，选定好类型。
- 创建table cell 的类并且绑定到视图上
- 进行变量声明，将视图变量拉到代码里面。
- 将数据传到界面上去
- 定义模型类，可以使用结构体，结构体初始化完成之后
- 定义数据，根据数据来动态改变每行的值，还有总共的row的数目
- 写用户点击之后的响应函数：

```swift
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        todos[indexPath.row].isChecked = !todos[indexPath.row].isChecked // 修改数据中是否被惦记的属性
        
        let cell = tableView.cellForRow(at: indexPath) as! TodosCell // 获取的点击的那个cell
        cell.checkMark.text = todos[indexPath.row].isChecked ?"√":"" //改变视图
        tableView.deselectRow(at: indexPath, animated: true)// 取消点击
        
    }
```

- 添加关于增加任务的视图，使用navigation viewCongtroller 实现页面的压栈，出栈的效果，使用show函数,进行页面的跳转
- navigation ViewController中是 navication bar 决定了最大的标题栏，然后要在后面的页面标题栏中自定义标题栏大小，需要添加 navication item
- 如果需要在标题栏添加按钮的话：添加控件 :BarButtonItem
- 实现添加任务的功能：
- 使用protocol和delegaate来实现反向传值，反向传的是新建任务的名字
- 利用委托模式，使得实现在todos界面，里面先添加到模型里面，然后再重写添加到视图里面。
- 第一响应，在界面加载完成之后，把响应直接转移到输入框，并且在点击完，缺点之后，使用navigationController。pop 出当前的界面；


```swift
// 绑定委托者
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "addTodo"{
            let vc = segue.destination as! AddTodoVC
            vc.delegate = self
        }

    //第一响应：
       todoInputTX.becomeFirstResponder()
    // sava点击函数
        @IBAction func saveTodo(_ sender: Any) {
        if let name = todoInputTX.text{
        delegate?.addTodo(name: name)
        }
        navigationController?.popViewController(animated: true)
    
    }
    //实现委托函数
        func addTodo(name: String) {
        todos.append(Todo(todo: name, isChecked: false))//添加数据到model里面。
        let indexPath = IndexPath(row: todos.count-1, section: 0)
        tableView.insertRows(at: [indexPath], with: .automatic)//添加一个新的todo Rows
        
    }


```
**注意事项：** 如果界面编辑完成之后，运行之后的界面和预期不一致，检查一下操作代码，是否修改界面，也就是先使用storyboard渲染界面，然后再用代码修改界面。

- 实现修改任务：
- 拉tableView Cell的Accessory action 拖拽 show 到另一页面（添加和修改）
- 给segue 指定 id 
- 正向传值，把点到的cell里面的值，传到修改的界面 在 prepare函数里面改
- 选择出指定id 的segue 在里面写函数，并且传值到修改界面里面，如果有值过去，也修改界面名字
- 另外完善反向传值的操作。用户点击去走另外一条代理的路线，然后绑定代理
- 在另外一条代理路线中，存到模型中去，然后找到对应的cell，更新视图。

```swift
// 另一个segue路径，传值过去
else if segue.identifier == "editTodo"{
            let vc = segue.destination as! AddTodoVC
            vc.delegate = self//代理绑定
            
            let cell = sender as! TodosCell
            let indexPath = tableView.indexPath(for: cell)!
            editRow = indexPath.row
            vc.editName = todos[editRow!].todo//传递参数
        }
// 实现edit 代理函数：
func editTodo(name: String) {
        todos[editRow!].todo = name//
        let indexPath = IndexPath(row: editRow!, section: 0)
        let cell = tableView.cellForRow(at: indexPath) as! TodosCell
        cell.todoLabel.text = todos[editRow!].todo
        
    }
//如果是从 edit 跳转过来，修改title，点击save执行另外一个代理：
  if editName != nil{
            navigationItem.title = "Edit Todo"
        }
      if let name = todoInputTX.text{
            if editName != nil {
                delegate?.editTodo(name: name)//走这个代理
            }else{
                delegate?.addTodo(name: name)
            }
            
        }
```

- p64
- 找到删除某一个row的代码，然后添加从模型删除数据的操作；
- 这样就实现的左划删除，
- 在代码中写右边的 bar button item 是一个edit item
- 然后去storyboard 中选择 tableview Editing 可以批量选择,修改点击事件在非edit情况下面进行。
- 修改默认汉字，一个是titleforDelete修改删除汉字。
- 一个是通过edit函数，修改显示按钮的title


```swift
//删除某一个row 实现左滑动删除
     override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
     if editingStyle == .delete {
        todos.remove(at: indexPath.row)//从模型中删除数据
     // Delete the row from the data source
     tableView.deleteRows(at: [indexPath], with: .fade)
     } else if editingStyle == .insert {
     // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
     }
//修改删除时候显示的文字：
    override func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAt indexPath: IndexPath) -> String? {
        return "删除"
    }
// 在代码中添加 editing btn，并且修改显示的title：
self.navigationItem.leftBarButtonItem = self.editButtonItem
        editButtonItem.title = "编辑"
    
    override func setEditing(_ editing: Bool, animated: Bool) {
        super.setEditing(editing, animated: animated)
        editButtonItem.title = isEditing ? "完成" : "编辑"
    }

```

- p65
- 批量删除，去添加一个删除按钮，拉出一个action，检测所有被选中的cell
- 然后for循环删除数据，然后 tableview.delete(),批量删除row
- 移动单元格，moveRowAt 方法，先采用先删除后插入移动数据，然后
- 使用tableView.moveRow()方法移动row

```swift
// 批量删除：
 @IBAction func deleteRows(_ sender: Any) {
        if let indexPaths = tableView.indexPathsForSelectedRows{
            for indexPath in indexPaths{
                todos.remove(at: indexPath.row)
            }//这个方法删除数据不安全
            tableView.beginUpdates()//提高更新性能
            tableView.deleteRows(at: indexPaths, with: .automatic)// 批量删除rows
            tableView.endUpdates()//提高更新性能
        }
    }
// 移动rows
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {
        // 模型移动数据
        let from = todos.remove(at: fromIndexPath.row)
        todos.insert(from, at: to.row)
        // view 进行移动
        tableView.moveRow(at: fromIndexPath, to: to)
    }

```

- 查看appDelegate文件，查看app的生命周期函数，了解调用顺序
- 本地存储，先编码，然后存储到沙盒里面，定为一个函数，每次更新数据之后，进行调用
- 解码，viewdidload（）里面继续即可
- 定义空数组，空字典的另一种写法：


```swift
// 编码，存储到本地plist里面：
    func saveData(){
        
        do{
            //编码
            let data = try JSONEncoder().encode(todos) 
            //存到本地，key为”todos“
            UserDefaults.standard.set(data, forKey: "todos")
        }catch{
            print(error)
        }
    }
// 从本地存储中取数据
        if let data = UserDefaults.standard.data(forKey: "todos"){
            do {
                // 数据解码成类。
                todos = try JSONDecoder().decode([Todo].self, from: data)
            }
            catch{
                print(error)
            }
        }
//定义空数组，空字典的另一种写法：
var todos = [Todo]()
var dic = [String:String]()
```