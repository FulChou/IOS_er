//
//  TodosViewController.swift
//  Todos
//
//  Created by 周福 on 2020/2/1.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit
import RealmSwift

class TodosViewController: UITableViewController {
    
    var todos:Results<Todo>?
    var editRow:Int?
    let realm = try! Realm()
    
    @IBOutlet weak var searchBar: UISearchBar!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        searchBar.delegate = self
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false
        
        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        self.navigationItem.leftBarButtonItem = self.editButtonItem
        editButtonItem.title = "编辑"
        print(FileManager.default.urls(for: .documentDirectory, in: .userDomainMask))//打印出当前存储所在的目录
        
        // userDefaults 取数据
        //        if let data = UserDefaults.standard.data(forKey: "todos"){
        //            do {
        //                // 数据解码成类。
        //                todos = try JSONDecoder().decode([Todo].self, from: data)
        //            }
        //            catch{
        //                print(error)
        //            }
        //        }
        
        // realm 取数据：
        todos = realm.objects(Todo.self).sorted(byKeyPath: "createDate", ascending: false)
        
        
    }
    // 存储数据，不仅仅到了数据库，内存里面的数据也跟着改变了
    func saveData(todo:Todo){
        
        //        do{
        //            let data = try JSONEncoder().encode(todos)
        //            UserDefaults.standard.set(data, forKey: "todos")
        //        }catch{
        //            print(error)
        //        }
        do {
            try realm.write {
                realm.add(todo)
            }
        } catch  {
            print(error)
        }
        
    }
    
    //    func updateData(todo:Todo,inrow row:Int){
    //        do {
    //                   try realm.write {
    //                    todos![row].isChecked = todo.isChecked                   }
    //               } catch {
    //                   print(error)
    //               }
    //    }
    
    override func setEditing(_ editing: Bool, animated: Bool) {
        super.setEditing(editing, animated: animated)
        editButtonItem.title = isEditing ? "完成" : "编辑"
    }
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return todos?.count ?? 0
    }
    
    @IBAction func deleteRows(_ sender: Any) {
        
        //        if let indexPaths = tableView.indexPathsForSelectedRows{
        //            for indexPath in indexPaths{
        //                todos.remove(at: indexPath.row)
        //            }//这个方法删除数据不安全
        ////            saveData()
        //            tableView.beginUpdates()//提高更新性能
        //            tableView.deleteRows(at: indexPaths, with: .automatic)// 批量删除rows
        //            tableView.endUpdates()//提高更新性能
        //        }
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "todo", for: indexPath) as! TodosCell
        if let todos = todos{
            cell.checkMark.text = todos[indexPath.row].isChecked ?"√":""
            cell.todoLabel.text = todos[indexPath.row].name
        }
        
        
        return cell
    }
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if !isEditing{
            if let todos = todos{
                //                todos[indexPath.row].isChecked = !todos[indexPath.row].isChecked // 修改数据中是否被惦记的属性
                //            saveData()
                
                // change data all model and database
                do {
                    try realm.write {
                        todos[indexPath.row].isChecked = !todos[indexPath.row].isChecked                   }
                } catch {
                    print(error)
                }
                
                tableView.reloadData() //改变视图
                //                let cell = tableView.cellForRow(at: indexPath) as! TodosCell // 获取的点击的那个cell
                //                cell.checkMark.text = todos[indexPath.row].isChecked ?"√":"" //改变视图
                
                tableView.deselectRow(at: indexPath, animated: true)// 取消点击
            }
            
        }
        
    }
    
    /*
     // Override to support conditional editing of the table view.
     override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
     // Return false if you do not want the specified item to be editable.
     return true
     }
     */
    
    
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            do {
                try realm.write {
                    realm.delete(todos![indexPath.row])
                }
            } catch  {
                print(error)
            }
            //        saveData()
            tableView.reloadData()
            // Delete the row from the data source
            //             tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }
        
    }
    override func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAt indexPath: IndexPath) -> String? {
        return "删除"
    }
    
    
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {
        //        // 模型移动数据
        //        let from = todos.remove(at: fromIndexPath.row)
        //        todos.insert(from, at: to.row)
        ////        saveData()
        //        // view 进行移动
        //        tableView.moveRow(at: fromIndexPath, to: to)
    }
    
    
    /*
     // Override to support conditional rearranging of the table view.
     override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
     // Return false if you do not want the item to be re-orderable.
     return true
     }
     */
    
    
    // MARK: - Navigation
    
    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "addTodo"{
            let vc = segue.destination as! AddTodoVC
            vc.delegate = self
            
        }else if segue.identifier == "editTodo"{
            let vc = segue.destination as! AddTodoVC
            vc.delegate = self//代理绑定
            
            let cell = sender as! TodosCell
            let indexPath = tableView.indexPath(for: cell)!
            editRow = indexPath.row
            vc.editName = todos![editRow!].name//传递参数
        }
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    
    
}
extension TodosViewController:AddTodoDelegate,UISearchBarDelegate{
    
    func addTodo(name: String) {
        //Todo(
        //        todos.append(Todo(name: name, isChecked: false))//新增数据
        let todo = Todo()
        todo.name = name
        //        todos.append(todo)
        saveData(todo: todo)//存储新增数据，模型里面的数据也增加了
        
        tableView.reloadData() //重新执行渲染方法
        //        let indexPath = IndexPath(row: todos.count-1, section: 0)
        //        tableView.insertRows(at: [indexPath], with: .automatic)
        
    }
    func editTodo(name: String) {
        //        todos[editRow!].name = name//修改数据
        ////        saveData()
        //        let indexPath = IndexPath(row: editRow!, section: 0)
        //        let cell = tableView.cellForRow(at: indexPath) as! TodosCell
        //        cell.todoLabel.text = todos[editRow!].name
        // 修改数据，重新渲染加载数据：
        do {
            try realm.write {
                todos![editRow!].name = name
            }
        } catch {
            print(error)
        }
        tableView.reloadData()
    }
    
    // MARK- ui search bar delegate:
    func searchBarSearchButtonClicked(_ searchBar: UISearchBar) {
        
        // realm 取数据：
        todos = realm.objects(Todo.self)
        
        todos = todos?.filter("name CONTAINS %@", searchBar.text!).sorted(byKeyPath: "createDate", ascending: false)
        
        tableView.reloadData()
    }
    
    func searchBarTextDidEndEditing(_ searchBar: UISearchBar) {
    }
    
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        if searchBar.text!.isEmpty{
            todos = realm.objects(Todo.self)
            tableView.reloadData()
            
            DispatchQueue.main.async {
                searchBar.resignFirstResponder()//失去第一响应
            }
        }
        
    }
}
