/**
 * 621. 任务调度器
 * 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
 * 任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
 * 
 * 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
 * 
 * 你需要计算完成所有任务所需要的最短时间。
 * @link https://leetcode-cn.com/problems/task-scheduler/
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function (tasks, n) {
    // 算出每个任务数量
    let counts = Array(26).fill(0)
    tasks.forEach(val => counts[val.charCodeAt() - 'A'.charCodeAt()]++)
    counts.sort((a, b) => b - a)
    // 至少需要执行的次数
    let maxCount = counts[0]
    let retCount = (maxCount - 1) * (n + 1) + 1
    let i = 1
    while (i >=0 && counts[i] == maxCount) {
        retCount++
        i++
    }
    return Math.max(retCount, tasks.length)
};

let res = leastInterval(["A", "A", "A", "B", "B", "B"], 2)
//8
console.log(res)

