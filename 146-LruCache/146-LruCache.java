// Last updated: 2/28/2026, 4:28:20 PM
import java.util.HashMap;


public class LRUCache {

class DLinkedNode {
  int key;
  int value;
  DLinkedNode prev;
  DLinkedNode next;
}

private void addNode(DLinkedNode node) {
  node.prev = head;
  node.next = head.next;

  head.next.prev = node;
  head.next = node;
}

private void removeNode(DLinkedNode node){
  DLinkedNode prev = node.prev;
  DLinkedNode next = node.next;

  prev.next = next;
  next.prev = prev;
}

private void moveToHead(DLinkedNode node){
  this.removeNode(node);
  this.addNode(node);
}

private DLinkedNode popTail(){
  DLinkedNode res = tail.prev;
  this.removeNode(res);
  return res;
}

private HashMap<Integer, DLinkedNode> 
  cache = new HashMap<Integer, DLinkedNode>();
private int count;
private int capacity;
private DLinkedNode head, tail;

public LRUCache(int capacity) {
  this.count = 0;
  this.capacity = capacity;

  head = new DLinkedNode();
  head.prev = null;

  tail = new DLinkedNode();
  tail.next = null;

  head.next = tail;
  tail.prev = head;
}

public int get(int key) {

  DLinkedNode node = cache.get(key);
  if(node == null){
    return -1; // should raise exception here.
  }

  // move the accessed node to the head;
  this.moveToHead(node);

  return node.value;
}


public void put(int key, int value) {
  DLinkedNode node = cache.get(key);

   

  if(node == null){

      
    if(count >= capacity){
      // pop the tail
      DLinkedNode tail = this.popTail();
      this.cache.remove(tail.key);
      --count;
   }


    DLinkedNode newNode = new DLinkedNode();
    newNode.key = key;
    newNode.value = value;

    this.cache.put(key, newNode);
    this.addNode(newNode);

    ++count;

   
  }else{
    // update the value.
    node.value = value;
    this.moveToHead(node);
  }
}

}