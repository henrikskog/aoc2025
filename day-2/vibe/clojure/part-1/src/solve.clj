(ns solve
  (:require [clojure.string :as str]))

(defn invalid-id? [s]
  "Check if a string has a repeating pattern (e.g., '1212' repeats '12')"
  (let [len (count s)]
    (some (fn [prefix-len]
            (let [prefix (subs s 0 prefix-len)
                  parts (str/split s (re-pattern (java.util.regex.Pattern/quote prefix)))]
              (every? str/blank? parts)))
          (range 1 len))))

(defn invalid-ids-in-range [a b]
  "Sum all invalid IDs in the range [a, b]"
  (reduce (fn [sum x]
            (if (invalid-id? (str x))
              (+ sum x)
              sum))
          0
          (range a (inc b))))

(defn parse-range [range-str]
  "Parse a range string like '5529687-5587329' into [start end]"
  (let [[a b] (str/split range-str #"-")]
    [(Long/parseLong a) (Long/parseLong b)]))

(defn -main [& args]
  (let [input (str/trim (slurp "input.txt"))
        ranges (str/split input #",")
        result (reduce (fn [sum range-str]
                         (let [[a b] (parse-range range-str)]
                           (+ sum (invalid-ids-in-range a b))))
                       0
                       ranges)]
    (println result)))
