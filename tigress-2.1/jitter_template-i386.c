/*
 * MyJIT 
 * Copyright (C) 2010 Petr Krajca, <krajcap@inf.upol.cz>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */
#include<assert.h>
#include<ctype.h>
//#include<dlfcn.h>
#include<limits.h>
#include<stdarg.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/mman.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<unistd.h>
#define JITLIB_CORE_H
#define FR_IMM	(jit_mkreg(JIT_RTYPE_FLOAT, JIT_RTYPE_IMM, 0))
#define R_IMM	(jit_mkreg(JIT_RTYPE_INT, JIT_RTYPE_IMM, 0)) // used by amd64 and sparc
#define GET_OP(op) ((jit_opcode) (op->code & 0xfff8))
#define GET_OP_SUFFIX(op) (op->code & 0x0007)
#define IS_IMM(op) (op->code & IMM)
#define IS_SIGNED(op) (!(op->code & UNSIGNED))
#define ARG_TYPE(op, arg) (((op)->spec >> ((arg) - 1) * 2) & 0x03)
#define JIT_BUFFER_OFFSET(jit)       ((jit_value)jit->ip - (jit_value)jit->buf)
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define TRACE_PREV      (1)
#define TRACE_NEXT      (2)
#define R(x) (jit_mkreg(JIT_RTYPE_INT, JIT_RTYPE_REG, (x)))
#define FR(x) (jit_mkreg(JIT_RTYPE_FLOAT, JIT_RTYPE_REG, (x)))
typedef long jit_value;
typedef unsigned long jit_unsigned_value;
typedef double jit_float;
void *malloc(size_t size);
void free(void *ptr);
void *realloc(void *ptr, size_t size);
struct jit_tree;
struct jit_set;
struct jit_rmap;
struct jit_debug_info;
typedef struct jit_op {
        unsigned short code;
        unsigned char spec;
        unsigned char arg_size;
        unsigned char assigned;
        unsigned char fp;
 unsigned char in_use;
        double flt_imm;
        jit_value arg[3];
        jit_value r_arg[3];
        long patch_addr;
        struct jit_op * jmp_addr;
        struct jit_op * next;
        struct jit_op * prev;
        struct jit_set * live_in;
        struct jit_set * live_out;
        struct jit_rmap * regmap;
        int normalized_pos;
        struct jit_tree * allocator_hints;
 struct jit_debug_info *debug_info;
 unsigned long code_offset;
 unsigned long code_length;
 void *addendum;
} jit_op;
typedef struct jit_label {
        long pos;
        jit_op * op;
        struct jit_label * next;
} jit_label;
typedef jit_value jit_reg;
union jit_proc_value_alias {
        void (*ptr)();
        jit_value num;
};
static inline jit_value jit_proc_value(void (*f)(void))
{
 union jit_proc_value_alias alias;
 alias.ptr = f;
 return alias.num;
}
enum jit_inp_type {
 JIT_SIGNED_NUM,
 JIT_UNSIGNED_NUM,
 JIT_FLOAT_NUM,
 JIT_PTR
};
enum jit_warning {
 JIT_WARN_DEAD_CODE = 0x00000001,
 JIT_WARN_OP_WITHOUT_EFFECT = 0x00000002,
 JIT_WARN_INVALID_DATA_SIZE = 0x00000004,
 JIT_WARN_UNINITIALIZED_REG = 0x00000008,
 JIT_WARN_UNALIGNED_CODE = 0x00000010,
 JIT_WARN_INVALID_CODE_REFERENCE = 0x00000020,
 JIT_WARN_INVALID_DATA_REFERENCE = 0x00000040,
 JIT_WARN_MISSING_PATCH = 0x00000080,
 JIT_WARN_REGISTER_TYPE_MISMATCH = 0x00000100,
 JIT_WARN_ALL = 0x7fffffff
};
struct jit * jit_init();
struct jit_op * jit_add_op(struct jit * jit, unsigned short code, unsigned char spec, jit_value arg1, jit_value arg2, jit_value arg3, unsigned char arg_sizee, struct jit_debug_info *debug_info);
struct jit_op * jit_add_fop(struct jit * jit, unsigned short code, unsigned char spec, jit_value arg1, jit_value arg2, jit_value arg3, double flt_imm, unsigned char arg_sizee, struct jit_debug_info *debug_info);
struct jit_debug_info *jit_debug_info_new(const char *filename, const char *function, int lineno);
void jit_generate_code(struct jit * jit);
void jit_free(struct jit * jit);
void jit_dump_ops(struct jit * jit, int verbosity);
void jit_check_code(struct jit *jit, int warnings);
void jit_trace(struct jit *jit, int verbosity);
void jit_enable_optimization(struct jit * jit, int opt);
void jit_disable_optimization(struct jit * jit, int opt);
jit_op * jit_add_prolog(struct jit *, void *, struct jit_debug_info *);
jit_label * jit_get_label(struct jit * jit);
int jit_allocai(struct jit * jit, int size);
jit_op *jit_data_bytes(struct jit *jit, jit_value count, unsigned char *data)
{
 jit_op *op = jit_add_op(jit, JIT_DATA_BYTES | 0x02, (((0x00) << 4) | ((0x00) << 2) | (0x02)), count, 0, 0, 0, NULL);
 op->addendum = malloc(count);
 memcpy(op->addendum, data, count);
 return op;
}
int jit_regs_active_count(jit_op *op);
void jit_regs_active(jit_op *op, jit_value *dest);
typedef jit_value jit_tree_key;
typedef void * jit_tree_value;
typedef struct jit_tree {
 struct jit_tree * left;
 struct jit_tree * right;
 int color;
 jit_tree_key key;
 jit_tree_value value;
} jit_tree;
static inline int jit_internal_is_red(jit_tree * n)
{
 if (n == NULL) return 0;
 return (n->color == (1));
}
static inline jit_tree * jit_internal_rotate_left(jit_tree * h)
{
 jit_tree * x = h->right;
 h->right = x->left;
 x->left = h;
 x->color = x->left->color;
 x->left->color = (1);
 return x;
}
static inline jit_tree * jit_internal_rotate_right(jit_tree * h)
{
 jit_tree * x = h->left;
 h->left = x->right;
 x->right = h;
 x->color = x->right->color;
 x->right->color = (1);
 return x;
}
static inline void jit_internal_color_flip(jit_tree * h)
{
 h->color = !h->color;
 h->left->color = !h->left->color;
 h->right->color = !h->right->color;
}
static inline jit_tree * jit_internal_fixup(jit_tree * h)
{
 if (jit_internal_is_red(h->right)) h = jit_internal_rotate_left(h);
 if (jit_internal_is_red(h->left) && (jit_internal_is_red(h->left->left))) {
  h = jit_internal_rotate_right(h);
  jit_internal_color_flip(h);
 }
 if (jit_internal_is_red(h->left) && jit_internal_is_red(h->right)) jit_internal_color_flip(h);
 return h;
}
static inline jit_tree * jit_internal_node_new(jit_tree_key key, jit_tree_value value)
{
 jit_tree * res = malloc(sizeof(jit_tree));
 res->key = key;
 res->value = value;
 res->color = (1);
 res->left = NULL;
 res->right = NULL;
 return res;
}
static jit_tree * jit_internal_node_insert(jit_tree * h, jit_tree_key key, jit_tree_value value, int * found)
{
 if (h == NULL) return jit_internal_node_new(key, value);
 if (jit_internal_is_red(h->left) && jit_internal_is_red(h->right)) jit_internal_color_flip(h);
 if (h->key == key) {
  h->value = value;
  if (found) *found = 1;
 } else if (h->key > key) h->left = jit_internal_node_insert(h->left, key, value, found);
 else h->right = jit_internal_node_insert(h->right, key, value, found);
 return jit_internal_fixup(h);
}
static jit_tree * jit_tree_insert(jit_tree * root, jit_tree_key key, jit_tree_value value, int * found)
{
 if (found) *found = 0;
 root = jit_internal_node_insert(root, key, value, found);
 root->color = (0);
 return root;
}
static jit_tree * jit_tree_search(jit_tree * h, jit_tree_key key)
{
 if ((h == NULL) || (h->key == key)) return h;
 if (h->key > key) return jit_tree_search(h->left, key);
 return jit_tree_search(h->right, key);
}
static inline jit_tree * jit_internal_move_red_left(jit_tree * h)
{
 jit_internal_color_flip(h);
 if (jit_internal_is_red(h->right->left)) {
  h->right = jit_internal_rotate_right(h->right);
  h = jit_internal_rotate_left(h);
  jit_internal_color_flip(h);
 }
 return h;
}
static inline jit_tree * jit_internal_move_red_right(jit_tree * h)
{
 jit_internal_color_flip(h);
 if (jit_internal_is_red(h->left->left)) {
  h = jit_internal_rotate_right(h);
  jit_internal_color_flip(h);
 }
 return h;
}
static inline jit_tree_key jit_internal_node_min(jit_tree * x)
{
 if (x->left == NULL) return x->key;
 else return jit_internal_node_min(x->left);
}
static jit_tree * jit_internal_delete_min(jit_tree * h)
{
 if (h->left == NULL) {
  free(h);
  return NULL;
 }
 if ((!jit_internal_is_red(h->left)) && (!jit_internal_is_red(h->left->left)))
  h = jit_internal_move_red_left(h);
 h->left = jit_internal_delete_min(h->left);
 return jit_internal_fixup(h);
}
static jit_tree * jit_internal_delete_node(jit_tree * h, jit_tree_key key, int * found)
{
 if (h == NULL) {
  if (found) *found = 0;
  return NULL;
 }
 if (key < h->key) {
  if ((!jit_internal_is_red(h->left)) && (h->left) && (!jit_internal_is_red(h->left->left)))
   h = jit_internal_move_red_left(h);
  h->left = jit_internal_delete_node(h->left, key, found);
 } else {
  if (jit_internal_is_red(h->left)) h = jit_internal_rotate_right(h);
  if ((key == h->key) && (h->right == NULL)) {
   free(h);
   if (found) *found = 1;
   return NULL;
  }
  if (!jit_internal_is_red(h->right) && (h->right) && !jit_internal_is_red(h->right->left)) h = jit_internal_move_red_right(h);
  if (key == h->key) {
   h->value = jit_tree_search(h->right, jit_internal_node_min(h->right))->value;
   h->key = jit_internal_node_min(h->right);
   h->right = jit_internal_delete_min(h->right);
   if (found) *found = 1;
  }
  else h->right = jit_internal_delete_node(h->right, key, found);
 }
 return jit_internal_fixup(h);
}
static inline jit_tree * jit_tree_delete(jit_tree * root, jit_tree_key key, int * found)
{
 root = jit_internal_delete_node(root, key, found);
 if (root) root->color = (0);
 return root;
}
static inline jit_tree * jit_tree_addall(jit_tree * target, jit_tree * n)
{
 if (n == NULL) return target;
 target = jit_tree_addall(target, n->left);
 target = jit_tree_insert(target, n->key, n->value, NULL);
 target = jit_tree_addall(target, n->right);
 return target;
}
static inline jit_tree * jit_tree_clone(jit_tree * root)
{
 return jit_tree_addall(NULL, root);
}
static void jit_tree_walk(jit_tree *h, void (*func)(jit_tree_key key, jit_tree_value value, void *thunk), void *thunk)
{
        if (!h) return;
 jit_tree_walk(h->left, func, thunk);
        func(h->key, h->value, thunk);
 jit_tree_walk(h->right, func, thunk);
}
static inline void jit_print_tree(jit_tree * h, int level)
{
 if (h == NULL) return;
 for (int i = 0; i < level; i++)
  printf(" ");
 printf("%i:%li\n", (int)h->key, (long)h->value);
 jit_print_tree(h->left, level + 1);
 jit_print_tree(h->right, level + 1);
}
static void jit_tree_free(jit_tree * h)
{
 if (h == NULL) return;
 jit_tree_free(h->left);
 jit_tree_free(h->right);
 free(h);
}
static int jit_tree_subset(jit_tree * root, jit_tree * n)
{
 if (n == NULL) return 1;
 return jit_tree_search(root, n->key) && jit_tree_subset(root, n->left) && jit_tree_subset(root, n->right);
}
static int jit_tree_equal(jit_tree * r1, jit_tree * r2)
{
 return jit_tree_subset(r1, r2) && jit_tree_subset(r2, r1);
}
static int jit_tree_size(jit_tree *h)
{
 if (h == NULL) return 0;
 return jit_tree_size(h->left) + jit_tree_size(h->right) + 1;
}
typedef struct {
 int id;
 char * name;
 char callee_saved;
 char fp;
 short priority;
} jit_hw_reg;
struct jit_reg_allocator {
 int gp_reg_cnt;
 int fp_reg_cnt;
 int fp_reg;
 int gp_arg_reg_cnt;
 int fp_arg_reg_cnt;
 jit_hw_reg * ret_reg;
 jit_hw_reg * fpret_reg;
 jit_hw_reg * gp_regs;
 jit_hw_reg * fp_regs;
 jit_hw_reg ** gp_arg_regs;
 jit_hw_reg ** fp_arg_regs;
 struct jit_func_info * current_func_info;
};
typedef struct jit_rmap {
 jit_tree * map;
} jit_rmap;
struct jit_allocator_hint {
 int last_pos;
 int should_be_calleesaved;
 int should_be_eax;
 int refs;
};
typedef struct jit_prepared_args {
 int count;
 int ready;
 int gp_args;
 int fp_args;
 int stack_size;
 jit_op * op;
 struct jit_out_arg {
  union {
   long generic;
   double fp;
  } value;
  int argpos;
  char isreg;
  char isfp;
  char size;
 } * args;
} jit_prepared_args;
typedef struct jit_set {
 jit_tree * root;
} jit_set;
struct jit_func_info {
 int general_arg_cnt;
 int float_arg_cnt;
 long allocai_mem;
 int arg_capacity;
 struct jit_inp_arg {
  enum jit_inp_type type;
  int size;
  char passed_by_reg;
  union {
   int reg;
   int stack_pos;
  } location;
  int spill_pos;
  int gp_pos;
  int fp_pos;
  int overflow;
  int phys_reg;
 } * args;
 int gp_reg_count;
 int fp_reg_count;
 int has_prolog;
 struct jit_op *first_op;
};
struct jit {
 unsigned char * buf;
 unsigned int buf_capacity;
 unsigned char * ip;
 struct jit_op * ops;
 struct jit_op * last_op;
 struct jit_reg_allocator * reg_al;
 struct jit_op * current_func;
 jit_label * labels;
 jit_prepared_args prepared_args;
 int push_count;
 unsigned int optimizations;
 unsigned char mmaped_buf;
};
struct jit_debug_info {
        const char *filename;
 const char *function;
        int lineno;
        int warnings;
};
void jit_patch_external_calls(struct jit * jit);
void jit_patch_local_addrs(struct jit *jit);
void jit_collect_statistics(struct jit * jit);
void jit_optimize_st_ops(struct jit * jit);
int jit_optimize_join_addmul(struct jit * jit);
int jit_optimize_join_addimm(struct jit * jit);
void jit_optimize_frame_ptr(struct jit * jit);
void jit_optimize_unused_assignments(struct jit * jit);
static int jit_internal_is_cond_branch_op(jit_op *op);
static inline void jit_set_free(jit_set * s);
void jit_trace_callback(struct jit *jit, jit_op *op, int verbosity, int trace);
void jit_init_arg_params(struct jit * jit, struct jit_func_info * info, int argpos, int * phys_reg);
void jit_assign_regs(struct jit * jit);
struct jit_reg_allocator * jit_reg_allocator_create();
void jit_reg_allocator_free(struct jit_reg_allocator * a);
void jit_gen_op(struct jit * jit, jit_op * op);
char * jit_reg_allocator_get_hwreg_name(struct jit_reg_allocator * al, int reg);
int jit_reg_in_use(jit_op * op, int reg, int fp);
jit_hw_reg * jit_get_unused_reg(struct jit_reg_allocator * al, jit_op * op, int fp);
jit_hw_reg * jit_get_unused_reg_with_index(struct jit_reg_allocator * al, jit_op * op, int fp, int index);
void jit_internal_rmap_free(jit_rmap * regmap);
void jit_allocator_hints_free(jit_tree *);
static struct jit_op * jit_op_new(unsigned short code, unsigned char spec, long arg1, long arg2, long arg3, unsigned char arg_size)
{
 struct jit_op * r = malloc(sizeof(struct jit_op));
 r->code = code;
 r->spec = spec;
 r->fp = 0;
 r->arg[0] = arg1;
 r->arg[1] = arg2;
 r->arg[2] = arg3;
 r->r_arg[0] = -1;
 r->r_arg[1] = -1;
 r->r_arg[2] = -1;
 r->assigned = 0;
 r->in_use = 1;
 r->arg_size = arg_size;
 r->next = NULL;
 r->prev = NULL;
 r->patch_addr = 0;
 r->jmp_addr = NULL;
 r->regmap = NULL;
 r->live_in = NULL;
 r->live_out = NULL;
 r->allocator_hints = NULL;
 r->debug_info = NULL;
 r->addendum = NULL;
 return r;
}
static inline void jit_op_append(jit_op * op, jit_op * appended)
{
 appended->next = op->next;
 if (op->next != NULL) op->next->prev = appended;
 appended->prev = op;
 op->next = appended;
}
static inline void jit_op_prepend(jit_op * op, jit_op * prepended)
{
 prepended->prev = op->prev;
 if (op->prev != NULL) op->prev->next = prepended;
 prepended->next = op;
 op->prev = prepended;
}
static inline jit_op * jit_op_first(jit_op * op)
{
 while (op->prev != NULL) op = op->prev;
 return op;
}
static inline jit_op * jit_op_last(jit_op * op)
{
 while (op->next != NULL) op = op->next;
 return op;
}
static inline void jit_free_op(struct jit_op *op)
{
        if (op->live_in) jit_set_free(op->live_in);
        if (op->live_out) jit_set_free(op->live_out);
        jit_internal_rmap_free(op->regmap);
        jit_allocator_hints_free(op->allocator_hints);
 if (op->debug_info) free(op->debug_info);
        if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
                struct jit_func_info * info = (struct jit_func_info *)op->arg[1];
                free(info->args);
                free(info);
        }
        free(op);
}
static inline void jit_op_delete(jit_op *op)
{
 op->prev->next = op->next;
 if (op->next) op->next->prev = op->prev;
 jit_free_op(op);
}
static inline int jit_is_label(struct jit * jit, void * ptr)
{
 jit_label * lab = jit->labels;
 while (1) {
  if (lab == NULL) return 0;
  if (lab == ptr) return 1;
  lab = lab->next;
 }
}
static inline struct jit_func_info * jit_current_func_info(struct jit * jit)
{
 return (struct jit_func_info *)(jit->current_func->arg[1]);
}
static inline void jit_internal_funcall_prepare(struct jit * jit, jit_op * op, int count)
{
 jit->prepared_args.args = malloc(sizeof(struct jit_out_arg) * count);
 jit->prepared_args.count = count;
 jit->prepared_args.ready = 0;
 jit->prepared_args.stack_size = 0;
 jit->prepared_args.op = op;
 jit->prepared_args.gp_args = 0;
 jit->prepared_args.fp_args = 0;
}
static inline void jit_internal_funcall_put_arg(struct jit * jit, jit_op * op)
{
 int pos = jit->prepared_args.ready;
 struct jit_out_arg * arg = &(jit->prepared_args.args[pos]);
 arg->isreg = !(op->code & 0x02);
 arg->isfp = 0;
 arg->value.generic = op->arg[0];
 arg->argpos = jit->prepared_args.gp_args++;
 jit->prepared_args.ready++;
 if (jit->prepared_args.ready > jit->reg_al->gp_arg_reg_cnt)
  jit->prepared_args.stack_size += (sizeof(void *));
}
static inline void jit_internal_funcall_fput_arg(struct jit * jit, jit_op * op)
{
 int pos = jit->prepared_args.ready;
 struct jit_out_arg * arg = &(jit->prepared_args.args[pos]);
 arg->isreg = !(op->code & 0x02);
 arg->isfp = 1;
 arg->size = op->arg_size;
 arg->argpos = jit->prepared_args.fp_args++;
 if ((op->code & 0x02)) arg->value.fp = op->flt_imm;
 else arg->value.generic = op->arg[0];
 jit->prepared_args.ready++;
 if (jit->prepared_args.ready > jit->reg_al->fp_arg_reg_cnt) {
  jit->prepared_args.stack_size += op->arg_size;
 }
}
static inline jit_value jit_value_align(jit_value value, jit_value alignment)
{
 return (value + (alignment - 1)) & (- alignment);
}
static inline jit_set * jit_set_new()
{
 jit_set * s = malloc(sizeof(jit_set));
 s->root = NULL;
 return s;
}
static inline jit_set * jit_set_clone(jit_set * s)
{
 jit_set * clone = jit_set_new();
 clone->root = jit_tree_clone(s->root);
 return clone;
}
static inline void jit_set_free(jit_set * s)
{
 jit_tree_free(s->root);
 free(s);
}
static inline void jit_set_addall(jit_set * target, jit_set * s)
{
 target->root = jit_tree_addall(target->root, s->root);
}
static inline int jit_set_get(jit_set * s, int value)
{
 return (jit_tree_search(s->root, value) != NULL);
}
static inline void jit_set_add(jit_set * s, int value)
{
 s->root = jit_tree_insert(s->root, value, (void *)1, NULL);
}
static inline void jit_set_remove(jit_set * s, int value)
{
 s->root = jit_tree_delete(s->root, value, NULL);
}
static inline int jit_set_equal(jit_set * s1, jit_set * s2)
{
 return jit_tree_equal(s1->root, s2->root);
}
static inline int jit_set_size(jit_set *s)
{
 return jit_tree_size(s->root);
}
struct copy_target {
        jit_value *target;
        int index;
};
static void jit_internal_copy_reg_to_array(jit_tree_key key, jit_tree_value value, void *target)
{
        struct copy_target *t = target;
        t->target[t->index] = key;
        t->index++;
}
static inline void jit_set_to_array(jit_set *s, jit_value *dest)
{
 struct copy_target t;
 t.target = dest;
 t.index = 0;
 jit_tree_walk(s->root, jit_internal_copy_reg_to_array, &t);
}
typedef enum jit_x86_gp_regs {
 X86_EAX = 0,
 X86_ECX = 1,
 X86_EDX = 2,
 X86_EBX = 3,
 X86_ESP = 4,
 X86_EBP = 5,
 X86_ESI = 6,
 X86_EDI = 7,
 X86_NREG
} jit_internal_X86_Reg_No;
typedef enum jit_x86_fp_regs {
 X86_XMM0,
 X86_XMM1,
 X86_XMM2,
 X86_XMM3,
 X86_XMM4,
 X86_XMM5,
 X86_XMM6,
 X86_XMM7,
 X86_XMM_NREG
} jit_internal_X86_XMM_Reg_No;
typedef enum {
 X86_ADD = 0,
 X86_OR = 1,
 X86_ADC = 2,
 X86_SBB = 3,
 X86_AND = 4,
 X86_SUB = 5,
 X86_XOR = 6,
 X86_CMP = 7,
 X86_NALU
} jit_internal_X86_ALU_Opcode;
typedef enum {
 X86_SHLD,
 X86_SHLR,
 X86_ROL = 0,
 X86_ROR = 1,
 X86_RCL = 2,
 X86_RCR = 3,
 X86_SHL = 4,
 X86_SHR = 5,
 X86_SAR = 7,
 X86_NSHIFT = 8
} jit_internal_X86_Shift_Opcode;
typedef enum {
 X86_FADD = 0,
 X86_FMUL = 1,
 X86_FCOM = 2,
 X86_FCOMP = 3,
 X86_FSUB = 4,
 X86_FSUBR = 5,
 X86_FDIV = 6,
 X86_FDIVR = 7,
 X86_NFP = 8
} jit_internal_X86_FP_Opcode;
typedef enum {
 jit_internal_X86_CC_EQ = 0, jit_internal_X86_CC_E = 0, jit_internal_X86_CC_Z = 0,
 jit_internal_X86_CC_NE = 1, jit_internal_X86_CC_NZ = 1,
 jit_internal_X86_CC_LT = 2, jit_internal_X86_CC_B = 2, jit_internal_X86_CC_C = 2, jit_internal_X86_CC_NAE = 2,
 jit_internal_X86_CC_LE = 3, jit_internal_X86_CC_BE = 3, jit_internal_X86_CC_NA = 3,
 jit_internal_X86_CC_GT = 4, jit_internal_X86_CC_A = 4, jit_internal_X86_CC_NBE = 4,
 jit_internal_X86_CC_GE = 5, jit_internal_X86_CC_AE = 5, jit_internal_X86_CC_NB = 5, jit_internal_X86_CC_NC = 5,
 jit_internal_X86_CC_LZ = 6, jit_internal_X86_CC_S = 6,
 jit_internal_X86_CC_GEZ = 7, jit_internal_X86_CC_NS = 7,
 jit_internal_X86_CC_P = 8, jit_internal_X86_CC_PE = 8,
 jit_internal_X86_CC_NP = 9, jit_internal_X86_CC_PO = 9,
 jit_internal_X86_CC_O = 10,
 jit_internal_X86_CC_NO = 11,
 X86_NCC
} jit_internal_X86_CC;
enum {
 X86_FP_C0 = 0x100,
 X86_FP_C1 = 0x200,
 X86_FP_C2 = 0x400,
 X86_FP_C3 = 0x4000,
 X86_FP_CC_MASK = 0x4500
};
enum {
 X86_FPCW_INVOPEX_MASK = 0x1,
 X86_FPCW_DENOPEX_MASK = 0x2,
 X86_FPCW_ZERODIV_MASK = 0x4,
 X86_FPCW_OVFEX_MASK = 0x8,
 X86_FPCW_UNDFEX_MASK = 0x10,
 X86_FPCW_PRECEX_MASK = 0x20,
 X86_FPCW_PRECC_MASK = 0x300,
 X86_FPCW_ROUNDC_MASK = 0xc00,
 X86_FPCW_PREC_SINGLE = 0,
 X86_FPCW_PREC_DOUBLE = 0x200,
 X86_FPCW_PREC_EXTENDED = 0x300,
 X86_FPCW_ROUND_NEAREST = 0,
 X86_FPCW_ROUND_DOWN = 0x400,
 X86_FPCW_ROUND_UP = 0x800,
 X86_FPCW_ROUND_TOZERO = 0xc00
};
typedef enum {
 X86_LOCK_PREFIX = 0xF0,
 X86_REPNZ_PREFIX = 0xF2,
 X86_REPZ_PREFIX = 0xF3,
 X86_REP_PREFIX = 0xF3,
 X86_CS_PREFIX = 0x2E,
 X86_SS_PREFIX = 0x36,
 X86_DS_PREFIX = 0x3E,
 X86_ES_PREFIX = 0x26,
 X86_FS_PREFIX = 0x64,
 X86_GS_PREFIX = 0x65,
 X86_UNLIKELY_PREFIX = 0x2E,
 X86_LIKELY_PREFIX = 0x3E,
 X86_OPERAND_PREFIX = 0x66,
 X86_ADDRESS_PREFIX = 0x67
} jit_internal_X86_Prefix;
static const unsigned char
jit_internal_x86_cc_unsigned_map [X86_NCC] = {
 0x74,
 0x75,
 0x72,
 0x76,
 0x77,
 0x73,
 0x78,
 0x79,
 0x7a,
 0x7b,
 0x70,
 0x71,
};
static const unsigned char
jit_internal_x86_cc_signed_map [X86_NCC] = {
 0x74,
 0x75,
 0x7c,
 0x7e,
 0x7f,
 0x7d,
 0x78,
 0x79,
 0x7a,
 0x7b,
 0x70,
 0x71,
};
typedef union {
 int val;
 unsigned char b [4];
} jit_internal_x86_imm_buf;
typedef enum {
 X86_SSE_SQRT = 0x51,
 X86_SSE_RSQRT = 0x52,
 X86_SSE_RCP = 0x53,
 X86_SSE_ADD = 0x58,
 X86_SSE_DIV = 0x5E,
 X86_SSE_MUL = 0x59,
 X86_SSE_SUB = 0x5C,
 X86_SSE_MIN = 0x5D,
 X86_SSE_MAX = 0x5F,
 X86_SSE_COMP = 0xC2,
 X86_SSE_AND = 0x54,
 X86_SSE_ANDN = 0x55,
 X86_SSE_OR = 0x56,
 X86_SSE_XOR = 0x57,
 X86_SSE_UNPCKL = 0x14,
 X86_SSE_UNPCKH = 0x15,
 X86_SSE_ADDSUB = 0xD0,
 X86_SSE_HADD = 0x7C,
 X86_SSE_HSUB = 0x7D,
 X86_SSE_MOVSHDUP = 0x16,
 X86_SSE_MOVSLDUP = 0x12,
 X86_SSE_MOVDDUP = 0x12,
 X86_SSE_SHUF = 0xC6,
 X86_SSE_COMI = 0x2F,
 X86_SSE_PAND = 0xDB,
 X86_SSE_POR = 0xEB,
 X86_SSE_PXOR = 0xEF,
 X86_SSE_PADDB = 0xFC,
 X86_SSE_PADDW = 0xFD,
 X86_SSE_PADDD = 0xFE,
 X86_SSE_PADDQ = 0xD4,
 X86_SSE_PSUBB = 0xF8,
 X86_SSE_PSUBW = 0xF9,
 X86_SSE_PSUBD = 0xFA,
 X86_SSE_PSUBQ = 0xFB,
 X86_SSE_PMAXSB = 0x3C,
 X86_SSE_PMAXSW = 0xEE,
 X86_SSE_PMAXSD = 0x3D,
 X86_SSE_PMAXUB = 0xDE,
 X86_SSE_PMAXUW = 0x3E,
 X86_SSE_PMAXUD = 0x3F,
 X86_SSE_PMINSB = 0x38,
 X86_SSE_PMINSW = 0xEA,
 X86_SSE_PMINSD = 0x39,
 X86_SSE_PMINUB = 0xDA,
 X86_SSE_PMINUW = 0x3A,
 X86_SSE_PMINUD = 0x3B,
 X86_SSE_PAVGB = 0xE0,
 X86_SSE_PAVGW = 0xE3,
 X86_SSE_PCMPEQB = 0x74,
 X86_SSE_PCMPEQW = 0x75,
 X86_SSE_PCMPEQD = 0x76,
 X86_SSE_PCMPEQQ = 0x29,
 X86_SSE_PCMPGTB = 0x64,
 X86_SSE_PCMPGTW = 0x65,
 X86_SSE_PCMPGTD = 0x66,
 X86_SSE_PCMPGTQ = 0x37,
 X86_SSE_PSADBW = 0xf6,
 X86_SSE_PSHUFD = 0x70,
 X86_SSE_PUNPCKLBW = 0x60,
 X86_SSE_PUNPCKLWD = 0x61,
 X86_SSE_PUNPCKLDQ = 0x62,
 X86_SSE_PUNPCKLQDQ = 0x6C,
 X86_SSE_PUNPCKHBW = 0x68,
 X86_SSE_PUNPCKHWD = 0x69,
 X86_SSE_PUNPCKHDQ = 0x6A,
 X86_SSE_PUNPCKHQDQ = 0x6D,
 X86_SSE_PACKSSWB = 0x63,
 X86_SSE_PACKSSDW = 0x6B,
 X86_SSE_PACKUSWB = 0x67,
 X86_SSE_PACKUSDW = 0x2B,
 X86_SSE_PADDUSB = 0xDC,
 X86_SSE_PADDUSW = 0xDD,
 X86_SSE_PSUBUSB = 0xD8,
 X86_SSE_PSUBUSW = 0xD9,
 X86_SSE_PADDSB = 0xEC,
 X86_SSE_PADDSW = 0xED,
 X86_SSE_PSUBSB = 0xE8,
 X86_SSE_PSUBSW = 0xE9,
 X86_SSE_PMULLW = 0xD5,
 X86_SSE_PMULLD = 0x40,
 X86_SSE_PMULHUW = 0xE4,
 X86_SSE_PMULHW = 0xE5,
 X86_SSE_PMULUDQ = 0xF4,
 X86_SSE_PMOVMSKB = 0xD7,
 X86_SSE_PSHIFTW = 0x71,
 X86_SSE_PSHIFTD = 0x72,
 X86_SSE_PSHIFTQ = 0x73,
 X86_SSE_SHR = 2,
 X86_SSE_SAR = 4,
 X86_SSE_SHL = 6,
 X86_SSE_PSRLW_REG = 0xD1,
 X86_SSE_PSRAW_REG = 0xE1,
 X86_SSE_PSLLW_REG = 0xF1,
 X86_SSE_PSRLD_REG = 0xD2,
 X86_SSE_PSRAD_REG = 0xE2,
 X86_SSE_PSLLD_REG = 0xF2,
 X86_SSE_PSRLQ_REG = 0xD3,
 X86_SSE_PSLLQ_REG = 0xF3,
 X86_SSE_PREFETCH = 0x18,
 X86_SSE_MOVNTPS = 0x2B,
  X86_SSE_MOVHPD_REG_MEMBASE = 0x16,
  X86_SSE_MOVHPD_MEMBASE_REG = 0x17,
  X86_SSE_MOVSD_REG_MEMBASE = 0x10,
  X86_SSE_MOVSD_MEMBASE_REG = 0x11,
 X86_SSE_PINSRB = 0x20,
 X86_SSE_PINSRW = 0xC4,
 X86_SSE_PINSRD = 0x22,
 X86_SSE_PEXTRB = 0x14,
 X86_SSE_PEXTRW = 0xC5,
 X86_SSE_PEXTRD = 0x16,
} jit_internal_X86_SSE_Opcode;
typedef enum {
 X86_SSE_CMP_EQ = 0,
 X86_SSE_CMP_LT = 1,
 X86_SSE_CMP_LE = 2,
 X86_SSE_CMP_UNORD = 3,
 X86_SSE_CMP_NEQ = 4,
 X86_SSE_CMP_NLT = 5,
 X86_SSE_CMP_NLE = 6,
 X86_SSE_CMP_ORD = 7
} jit_internal_X86_SSE_CmpCode;
static inline int jit_internal__bit_pop(unsigned int x) {
        x = (x & 0x55555555) + ((x >> 1) & 0x55555555);
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
        x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F);
        x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF);
        x = (x & 0x0000FFFF) + ((x >>16) & 0x0000FFFF);
        return x;
}
static int jit_internal_uses_hw_reg(struct jit_op * op, jit_value reg, int fp)
{
 if ((((jit_opcode) (op->code & 0xfff8)) == JIT_RENAMEREG) && (op->r_arg[0] == reg)) return 1;
 for (int i = 0; i < 3; i++)
  if (((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01) || ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03)) {
   if (fp && (((op->arg[i]) & 0x01) == (0))) continue;
   if (!fp && (((op->arg[i]) & 0x01) == (1))) continue;
   if (op->r_arg[i] == reg) return 1;
  }
 return 0;
}
static inline int jit_internal_is_spilled(jit_value arg_id, jit_op * prepare_op, int * reg);
static int jit_internal_emit_push_callee_saved_regs(struct jit * jit, jit_op * op);
static int jit_internal_emit_push_caller_saved_regs(struct jit * jit, jit_op * op);
static int jit_internal_emit_pop_callee_saved_regs(struct jit * jit);
static int jit_internal_emit_pop_caller_saved_regs(struct jit * jit, jit_op * op);
static void jit_internal_emit_save_all_regs(struct jit *jit, jit_op *op);
static void jit_internal_emit_restore_all_regs(struct jit *jit, jit_op *op);
static jit_hw_reg * jit_internal_rmap_is_associated(jit_rmap * rmap, int reg_id, int fp, jit_value * virt_reg);
static jit_hw_reg * jit_internal_rmap_get(jit_rmap * rmap, jit_value reg);
static unsigned char * jit_internal_emit_sse_get_sign_mask()
{
 static unsigned char bufx[32];
 unsigned char * buf = bufx + 1;
 while ((long)buf % 16) buf++;
 unsigned long long * bit_mask = (unsigned long long *)buf;
 *bit_mask = (unsigned long long)1 << 63;
 return buf;
}
static void jit_internal_emit_sse_alu_op(struct jit * jit, jit_op * op, int sse_op)
{
 if (op->r_arg[0] == op->r_arg[1]) {
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((sse_op)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((op->r_arg[0]))))&0x07)<<3)|((((((op->r_arg[2]))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 } else if (op->r_arg[0] == op->r_arg[2]) {
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((sse_op)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((op->r_arg[0]))))&0x07)<<3)|((((((op->r_arg[1]))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 } else {
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[1])))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((sse_op)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((op->r_arg[0]))))&0x07)<<3)|((((((op->r_arg[2]))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_change_sign(struct jit * jit, jit_op * op, int reg)
{
 do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0F; *(jit->ip)++ = (unsigned char)(X86_SSE_XOR); do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((reg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((((double *)jit_internal_emit_sse_get_sign_mask()))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
}
static void jit_internal_emit_sse_sub_op(struct jit * jit, jit_op * op, long a1, long a2, long a3)
{
 if (a1 == a2) {
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_SUB)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a1))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 } else if (a1 == a3) {
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_SUB)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a1))))&0x07)<<3)|((((((a2))))&0x07))); } while (0); } while (0); } while (0); } while (0);
  jit_internal_emit_sse_change_sign(jit, op, a1);
 } else {
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_SUB)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a1))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_div_op(struct jit * jit, long a1, long a2, long a3)
{
 if (a1 == a2) {
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_DIV)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a1))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 } else if (a1 == a3) {
  do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_DIV)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a2))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
  do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
 } else {
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xF2; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_DIV)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a1))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_neg_op(struct jit * jit, jit_op * op, long a1, long a2)
{
 if (a1 != a2) do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
 jit_internal_emit_sse_change_sign(jit, op, a1);
}
static void jit_internal_emit_sse_branch(struct jit * jit, jit_op * op, long a1, long a2, long a3, int x86_cond)
{
        do { *(jit->ip)++ = (unsigned char)0x66; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_COMI)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a2))))&0x07)<<3)|((((((a3))))&0x07))); } while (0); } while (0); } while (0); } while (0);
        op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
        do { int offset = ((!jit_is_label(jit, (void *)(a1)) ? (a1) : (((jit_value)jit->buf + ((jit_label *)(a1))->pos - (jit_value)jit->ip)))) - 6; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((x86_cond))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((x86_cond))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
}
static void jit_internal_emit_sse_round(struct jit * jit, jit_op * op, jit_value a1, jit_value a2)
{
 static const double x0 = 0.0;
 static const double x05 = 0.5;
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0F; *(jit->ip)++ = (unsigned char)(X86_SSE_COMI); do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((((double *)&x0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
 unsigned char * branch1 = jit->ip;
 do { int offset = (0) - 2; if ((((int)((offset)) >= -128 && (int)((offset)) <= 127))) do { if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_LT))]; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_LT))]; do { *(((jit->ip))) = (unsigned char)(((offset)) & 0xff); ++(((jit->ip))); } while (0); } while (0); else { offset -= 4; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_LT))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_LT))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } } while (0);
 do { *(jit->ip)++ = (unsigned char)0xF2; *(jit->ip)++ = (unsigned char)0x0F; *(jit->ip)++ = (unsigned char)(X86_SSE_ADD); do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((((double *)&x05))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
 unsigned char * branch2 = jit->ip;
 do { int t = (0) - 2; if ((((int)(t) >= -128 && (int)(t) <= 127))) { do { *((jit->ip))++ = (unsigned char)0xeb; do { *(((jit->ip))) = (unsigned char)(((t)) & 0xff); ++(((jit->ip))); } while (0); } while (0); } else { t -= 3; do { *((jit->ip))++ = (unsigned char)0xe9; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((t)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } } while (0);
 do { unsigned char* pos = (branch1) + 1; int disp, size = 0; switch (*(unsigned char*)(branch1)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = (jit->ip) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0xF2; *(jit->ip)++ = (unsigned char)0x0F; *(jit->ip)++ = (unsigned char)(X86_SSE_SUB); do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((((double *)&x05))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
 do { unsigned char* pos = (branch2) + 1; int disp, size = 0; switch (*(unsigned char*)(branch2)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = (jit->ip) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x2c; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
}
static void jit_internal_emit_sse_floor(struct jit * jit, jit_value a1, jit_value a2, int floor)
{
 int tmp_reg = (a2 == X86_XMM7 ? X86_XMM0 : X86_XMM7);
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((tmp_reg)))))&0x07)<<3)|(((((((tmp_reg)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x2c; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x2a; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((tmp_reg)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
 if (floor) {
  do { *(jit->ip)++ = (unsigned char)0x66; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_COMI)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((a2))))&0x07)<<3)|((((((tmp_reg))))&0x07))); } while (0); } while (0); } while (0); } while (0);
  do { if ((a1) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SBB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((0)) >= -128 && (int)((0)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SBB)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((0)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SBB)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 } else {
  do { *(jit->ip)++ = (unsigned char)0x66; do { *((jit->ip))++ = (unsigned char)0x0F; *((jit->ip))++ = (unsigned char)((X86_SSE_COMI)); do { do { *((((jit->ip))))++ = ((((3)&0x03)<<6)|((((((tmp_reg))))&0x07)<<3)|((((((a2))))&0x07))); } while (0); } while (0); } while (0); } while (0);
  do { if ((a1) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADC)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((0)) >= -128 && (int)((0)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADC)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((0)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADC)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 }
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
 do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((tmp_reg)))))&0x07)<<3)|(((((((tmp_reg)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
}
static void jit_internal_emit_sse_fst_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2)
{
 if (op->arg_size == sizeof(float)) {
  int live = jit_set_get(op->live_out, op->arg[1]);
  if (live) do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  if (live) do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a2)))))&0x07)<<3)|(((((((a2)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
 } else {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_fld_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2)
{
 if (op->arg_size == sizeof(float)) {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { if (((a2)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x10; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((a2)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_fldx_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2, jit_value a3)
{
 if (op->arg_size == sizeof(float)) {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
}
static void jit_internal_emit_sse_fstx_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2, jit_value a3)
{
 if (op->arg_size == sizeof(float)) {
  int live = jit_set_get(op->live_out, op->arg[2]);
  if (live) do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a3)))))&0x07)<<3)|(((((((a3)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a3)))&0x07))); } while (0); } while (0); } while (0);
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  if (live) do { do { *((jit->ip))++ = (unsigned char)0x66; do { *(((jit->ip)))++ = (unsigned char)0x0F; *(((jit->ip)))++ = (unsigned char)(((X86_SSE_SHUF))); do { do { *(((((jit->ip)))))++ = ((((3)&0x03)<<6)|(((((((a3)))))&0x07)<<3)|(((((((a3)))))&0x07))); } while (0); } while (0); } while (0); } while (0); *(jit->ip)++ = (unsigned char)(1); } while (0);
 } else {
  if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
}
static inline int jit_internal_GET_REG_POS(struct jit * jit, int r)
{
 if ((((r) >> 1) & 0x03) == (0)) {
  if (((r) & 0x01) == (0)) return (- (((((r) >> 4) & 0xfffffff) + 1) * (sizeof(void *))) - jit_current_func_info(jit)->allocai_mem);
  else return (- jit_current_func_info(jit)->gp_reg_count * (sizeof(void *)) - ((((r) >> 4) & 0xfffffff) + 1) * sizeof(jit_float) - jit_current_func_info(jit)->allocai_mem);
 } else assert(0);
}
void jit_optimize_st_ops(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_ST)
  && (op->prev)
  && (op->prev->code == (JIT_MOV | 0x02))
  && (op->arg[1] == op->prev->arg[0])
  && (((((long)(op->prev->arg[1])) >= INT32_MIN) && (((long)(op->prev->arg[1])) <= INT32_MAX)))
  && (!jit_set_get(op->live_out, op->arg[1])))
  {
   if (!(op->code & 0x02)) {
    op->code = JIT_X86_STI | 0x01;
    op->spec = (((0x00) << 4) | ((0x02) << 2) | (0x01));
   } else {
    op->code = JIT_X86_STI | 0x02;
    op->spec = (((0x00) << 4) | ((0x02) << 2) | (0x02));
   }
   op->arg[1] = op->prev->arg[1];
   op->prev->code = JIT_NOP;
   op->prev->spec = (((0x00) << 4) | ((0x00) << 2) | (0x00));
  }
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_STX)
  && (op->prev)
  && (op->prev->code == (JIT_MOV | 0x02))
  && (op->arg[2] == op->prev->arg[0])
  && (((((long)(op->prev->arg[1])) >= INT32_MIN) && (((long)(op->prev->arg[1])) <= INT32_MAX)))
  && (!jit_set_get(op->live_out, op->arg[2])))
  {
   if (!(op->code & 0x02)) {
    op->code = JIT_X86_STXI | 0x01;
    op->spec = (((0x02) << 4) | ((0x01) << 2) | (0x01));
   } else {
    op->code = JIT_X86_STXI | 0x02;
    op->spec = (((0x02) << 4) | ((0x01) << 2) | (0x02));
   }
   op->arg[2] = op->prev->arg[1];
   op->prev->code = JIT_NOP;
   op->prev->spec = (((0x00) << 4) | ((0x00) << 2) | (0x00));
  }
 }
}
void jit_optimize_frame_ptr(struct jit * jit)
{
 if (!jit->optimizations & (0x01)) return;
 struct jit_func_info * info = NULL;
 int uses_frame_ptr = 0;
 for (jit_op * op = jit_op_first(jit->ops); ; op = op->next) {
  if (!op || ((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   if (info && !uses_frame_ptr) {
    info->has_prolog = 0;
    uses_frame_ptr = 0;
   }
   if (op) info = (struct jit_func_info *) op->arg[1];
  }
  if (!op) break;
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_ALLOCA) || (((jit_opcode) (op->code & 0xfff8)) == JIT_UREG) || (((jit_opcode) (op->code & 0xfff8)) == JIT_LREG) || (((jit_opcode) (op->code & 0xfff8)) == JIT_SYNCREG)) {
   uses_frame_ptr |= 1;
  }
 }
}
void jit_optimize_unused_assignments(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if ((((op)->spec >> ((1) - 1) * 2) & 0x03) == 0x03) {
   if ((((jit_opcode) (op->code & 0xfff8)) == JIT_ADDC) || (((jit_opcode) (op->code & 0xfff8)) == JIT_ADDX)
   || (((jit_opcode) (op->code & 0xfff8)) == JIT_SUBC) || (((jit_opcode) (op->code & 0xfff8)) == JIT_SUBX)) continue;
   if (!jit_set_get(op->live_out, op->arg[0])) {
    op->code = JIT_NOP;
    op->spec = (((0x00) << 4) | ((0x00) << 2) | (0x00));
   }
  }
 }
}
static inline void jit_internal_make_nop(jit_op * op)
{
 op->code = JIT_NOP;
 op->spec = (((0x00) << 4) | ((0x00) << 2) | (0x00));
}
static jit_op * jit_internal_get_related_op(jit_op * op, int result_reg)
{
 jit_op * nextop = op->next;
 if ((nextop->arg[0] != result_reg) && (jit_set_get(nextop->live_out, result_reg))) return NULL;
 int used = 0;
 for (int i = 0; i < 3; i++)
  if (((((nextop)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01) && (nextop->arg[i])) {
   used = 1;
   break;
  }
 if (used) return nextop;
 return NULL;
}
static int jit_internal_join_2ops(jit_op * op, int opcode1, int opcode2, int (* joinfn)(jit_op *, jit_op *))
{
 if (op->code == opcode1) {
  jit_value result_reg = op->arg[0];
  jit_op * nextop = jit_internal_get_related_op(op, result_reg);
  if (nextop && (nextop->code == opcode2)) return joinfn(op, nextop);
 }
 return 0;
}
static int jit_internal_shift_index(int arg)
{
 if (arg == 2) return 1;
 if (arg == 4) return 2;
 if (arg == 8) return 3;
 assert(0);
}
static inline int jit_internal_pow2(int arg)
{
 int r = 1;
 for (int i = 0; i < arg; i++)
  r *= 2;
 return r;
}
static inline int jit_internal_is_suitable_mul(jit_op * op)
{
 jit_value arg = op->arg[2];
 return ((((op->code == (JIT_MUL | 0x02)) && ((arg == 2) || (arg == 4) || (arg == 8))))
 || ((op->code == (JIT_LSH | 0x02)) && ((arg == 1) || (arg == 2) || (arg == 3))));
}
static inline int jit_internal_make_addmuli(jit_op * op, jit_op * nextop)
{
 nextop->code = JIT_X86_ADDMUL | 0x02;
 nextop->spec = (((0x02) << 4) | ((0x01) << 2) | (0x03));
 nextop->arg[1] = op->arg[1];
 nextop->arg_size = (((jit_opcode) (op->code & 0xfff8)) == JIT_MUL ? jit_internal_shift_index(op->arg[2]) : op->arg[2]);
 jit_internal_make_nop(op);
 return 1;
}
static int jit_internal_join_muli_addi(jit_op * op, jit_op * nextop)
{
 if (!((((long)(nextop->arg[2])) >= INT32_MIN) && (((long)(nextop->arg[2])) <= INT32_MAX))) return 0;
 if (!jit_internal_is_suitable_mul(op)) return 0;
 return jit_internal_make_addmuli(op, nextop);
}
static int jit_internal_join_muli_ori(jit_op * op, jit_op * nextop)
{
 if (!jit_internal_is_suitable_mul(op)) return 0;
 int max = (((jit_opcode) (op->code & 0xfff8)) == JIT_MUL) ? max = op->arg[2] : jit_internal_pow2(op->arg[2]);
 if ((nextop->arg[2] > 0) && (nextop->arg[2] < max)) return jit_internal_make_addmuli(op, nextop);
 else return 0;
}
static int jit_internal_join_muli_addr(jit_op * op, jit_op * nextop)
{
 if ((!jit_internal_is_suitable_mul(op) || (nextop->arg[1] == nextop->arg[2]))) return 0;
 jit_value add_reg = (nextop->arg[1] == op->arg[0]) ? nextop->arg[2] : nextop->arg[1];
 nextop->code = JIT_X86_ADDMUL | 0x01;
 nextop->spec = (((0x01) << 4) | ((0x01) << 2) | (0x03));
 nextop->arg[1] = add_reg;
 nextop->arg[2] = op->arg[1];
 nextop->arg_size = (((jit_opcode) (op->code & 0xfff8)) == JIT_MUL ? jit_internal_shift_index(op->arg[2]) : op->arg[2]);
 jit_internal_make_nop(op);
 return 1;
}
int jit_optimize_join_addmul(struct jit * jit)
{
 int change = 0;
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  change |= jit_internal_join_2ops(op, JIT_MUL | 0x02, JIT_ADD | 0x02, jit_internal_join_muli_addi);
  change |= jit_internal_join_2ops(op, JIT_LSH | 0x02, JIT_ADD | 0x02, jit_internal_join_muli_addi);
  change |= jit_internal_join_2ops(op, JIT_MUL | 0x02, JIT_ADD | 0x01, jit_internal_join_muli_addr);
  change |= jit_internal_join_2ops(op, JIT_LSH | 0x02, JIT_ADD | 0x01, jit_internal_join_muli_addr);
  change |= jit_internal_join_2ops(op, JIT_MUL | 0x02, JIT_OR | 0x02, jit_internal_join_muli_ori);
  change |= jit_internal_join_2ops(op, JIT_LSH | 0x02, JIT_OR | 0x02, jit_internal_join_muli_ori);
 }
 return change;
}
static int jit_internal_join_addr_addi(jit_op * op, jit_op * nextop)
{
 if (!((((long)(nextop->arg[2])) >= INT32_MIN) && (((long)(nextop->arg[2])) <= INT32_MAX))) return 0;
 jit_internal_make_nop(op);
 nextop->code = JIT_X86_ADDIMM;
 nextop->spec = (((0x01) << 4) | ((0x01) << 2) | (0x03));
 nextop->arg[2] = nextop->arg[2];
 memcpy(&nextop->flt_imm, &(nextop->arg[2]), sizeof(jit_value));
 nextop->arg[1] = op->arg[1];
 nextop->arg[2] = op->arg[2];
 return 1;
}
static int jit_internal_join_addi_addr(jit_op * op, jit_op * nextop)
{
 if (!((((long)(op->arg[2])) >= INT32_MIN) && (((long)(op->arg[2])) <= INT32_MAX))) return 0;
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_SUB) op->arg[2] = -op->arg[2];
 jit_internal_make_nop(op);
 nextop->code = JIT_X86_ADDIMM;
 nextop->spec = (((0x01) << 4) | ((0x01) << 2) | (0x03));
 if (nextop->arg[1] == nextop->arg[2]) op->arg[2] *= 2;
 memcpy(&nextop->flt_imm, &(op->arg[2]), sizeof(jit_value));
 if (nextop->arg[1] == op->arg[0]) nextop->arg[1] = op->arg[1];
 if (nextop->arg[2] == op->arg[0]) nextop->arg[2] = op->arg[1];
 return 1;
}
int jit_optimize_join_addimm(struct jit * jit)
{
 int change = 0;
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  change |= jit_internal_join_2ops(op, JIT_ADD | 0x01, JIT_ADD | 0x02, jit_internal_join_addr_addi);
  change |= jit_internal_join_2ops(op, JIT_ADD | 0x01, JIT_SUB | 0x02, jit_internal_join_addr_addi);
  change |= jit_internal_join_2ops(op, JIT_ADD | 0x02, JIT_ADD | 0x01, jit_internal_join_addi_addr);
  change |= jit_internal_join_2ops(op, JIT_SUB | 0x02, JIT_ADD | 0x01, jit_internal_join_addi_addr);
 }
 return change;
}
void jit_init_arg_params(struct jit * jit, struct jit_func_info * info, int p, int * phys_reg)
{
 struct jit_inp_arg * a = &(info->args[p]);
 if (p == 0) a->location.stack_pos = 8;
 else {
  struct jit_inp_arg * prev_a = &(info->args[p - 1]);
  int stack_shift = jit_value_align(prev_a->size, 4);
  a->location.stack_pos = prev_a->location.stack_pos + stack_shift;
 }
 a->spill_pos = a->location.stack_pos;
 a->passed_by_reg = 0;
 a->overflow = 0;
}
static int jit_internal_emit_arguments(struct jit * jit)
{
 int stack_correction = 0;
 struct jit_out_arg * args = jit->prepared_args.args;
 int sreg;
 for (int i = jit->prepared_args.ready - 1; i >= 0; i--) {
  long value = args[i].value.generic;
  if (!args[i].isfp) {
   if (!args[i].isreg) do { int _imm = (int) (args[i].value.generic); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
   else {
    if (jit_internal_is_spilled(value, jit->prepared_args.op, &sreg))
     do { *(jit->ip)++ = (unsigned char)0xff; do { if (((X86_EBP)) == X86_ESP) { if (((jit_internal_GET_REG_POS(jit, args[i].value.generic))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) >= -128 && (int)(((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((jit_internal_GET_REG_POS(jit, args[i].value.generic)))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((jit_internal_GET_REG_POS(jit, args[i].value.generic))) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) >= -128 && (int)(((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((jit_internal_GET_REG_POS(jit, args[i].value.generic)))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((jit_internal_GET_REG_POS(jit, args[i].value.generic)))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    else do { *(jit->ip)++ = (unsigned char)0x50 + (sreg); } while (0);
   }
   continue;
  }
  if (args[i].size == sizeof(double)) {
   if (args[i].isreg) {
    if (jit_internal_is_spilled(value, jit->prepared_args.op, &sreg)) {
     int pos = (- jit_current_func_info(jit)->gp_reg_count * (sizeof(void *)) - ((((args[i].value.generic) >> 4) & 0xfffffff) + 1) * sizeof(jit_float) - jit_current_func_info(jit)->allocai_mem);
     do { *(jit->ip)++ = (unsigned char)0xff; do { if (((X86_EBP)) == X86_ESP) { if (((pos + 4)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((pos + 4))) >= -128 && (int)(((pos + 4))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos + 4))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos + 4))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((pos + 4)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((pos + 4))) >= -128 && (int)(((pos + 4))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos + 4))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos + 4))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
     do { *(jit->ip)++ = (unsigned char)0xff; do { if (((X86_EBP)) == X86_ESP) { if (((pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((pos))) >= -128 && (int)(((pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((pos))) >= -128 && (int)(((pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    } else {
     do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((8)) >= -128 && (int)((8)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((8)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
     do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    }
   } else {
    int fl_val[2];
    memcpy(fl_val, &(args[i].value.fp), sizeof(double));
    do { int _imm = (int) (fl_val[1]); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
    do { int _imm = (int) (fl_val[0]); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
   }
   continue;
  }
  if (args[i].isreg) {
   if (jit_internal_is_spilled(value, jit->prepared_args.op, &sreg)) {
    int pos = (- jit_current_func_info(jit)->gp_reg_count * (sizeof(void *)) - ((((args[i].value.generic) >> 4) & 0xfffffff) + 1) * sizeof(jit_float) - jit_current_func_info(jit)->allocai_mem);
    do { *(jit->ip)++ = (1) ? (unsigned char)0xdd : (unsigned char)0xd9; do { if (((X86_EBP)) == X86_ESP) { if (((pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((pos))) >= -128 && (int)(((pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((pos))) >= -128 && (int)(((pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((4)) >= -128 && (int)((4)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((4)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
    do { *(jit->ip)++ = (0) ? (unsigned char)0xdd: (unsigned char)0xd9; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
   } else {
    do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((sreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    do { *(jit->ip)++ = (1) ? (unsigned char)0xdd : (unsigned char)0xd9; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((4)) >= -128 && (int)((4)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((4)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
    do { *(jit->ip)++ = (0) ? (unsigned char)0xdd: (unsigned char)0xd9; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
   }
  } else {
   int fl_val;
   float b = (float)args[i].value.fp;
   memcpy(&fl_val, &b, sizeof(float));
   do { int _imm = (int) (fl_val); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
  }
 }
 return stack_correction;
}
static void jit_internal_emit_funcall(struct jit * jit, struct jit_op * op, int imm)
{
 int stack_correction = jit_internal_emit_arguments(jit);
 if (!imm) {
  do { *(jit->ip)++ = (unsigned char)0xff; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((2))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
 } else {
  op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
  do { *(jit->ip)++ = (unsigned char)0xe8; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((int)((!jit_is_label(jit, (void *)(op->r_arg[0])) ? (op->r_arg[0]) : (((jit_value)jit->buf + ((jit_label *)(op->r_arg[0]))->pos - (jit_value)jit->ip))) - 4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
 }
 if (jit->prepared_args.stack_size + stack_correction)
  do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((jit->prepared_args.stack_size + stack_correction)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((jit->prepared_args.stack_size + stack_correction)) >= -128 && (int)((jit->prepared_args.stack_size + stack_correction)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((jit->prepared_args.stack_size + stack_correction)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((jit->prepared_args.stack_size + stack_correction)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 free(jit->prepared_args.args);
 jit->push_count -= jit_internal_emit_pop_caller_saved_regs(jit, op);
}
void jit_patch_external_calls(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if ((op->code == (JIT_CALL | 0x02)) && (!jit_is_label(jit, (void *)op->arg[0])))
   do { unsigned char* pos = (jit->buf + (long)op->patch_addr) + 1; int disp, size = 0; switch (*(unsigned char*)(jit->buf + (long)op->patch_addr)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = ((unsigned char *)op->arg[0]) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_MSG)
   do { unsigned char* pos = (jit->buf + (long)op->patch_addr) + 1; int disp, size = 0; switch (*(unsigned char*)(jit->buf + (long)op->patch_addr)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = ((unsigned char *)printf) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_TRACE)
   do { unsigned char* pos = (jit->buf + (long)op->patch_addr) + 1; int disp, size = 0; switch (*(unsigned char*)(jit->buf + (long)op->patch_addr)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = ((unsigned char *)jit_trace_callback) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
 }
}
static void jit_internal_emit_prolog_op(struct jit * jit, jit_op * op)
{
 jit->current_func = op;
 struct jit_func_info * info = jit_current_func_info(jit);
 int prolog = jit_current_func_info(jit)->has_prolog;
 while ((long)jit->ip % 8)
  do { *(jit->ip)++ = (unsigned char)0x90; } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 if (prolog) {
  do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EBP); } while (0);
  do { switch ((4)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EBP)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); } while (0);
 }
 int stack_mem = info->allocai_mem + info->gp_reg_count * (sizeof(void *)) + info->fp_reg_count * sizeof(double);
 if (prolog)
  do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_mem)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((stack_mem)) >= -128 && (int)((stack_mem)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((stack_mem)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_mem)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 jit->push_count = jit_internal_emit_push_callee_saved_regs(jit, op);
}
static void jit_internal_emit_msg_op(struct jit * jit, jit_op * op)
{
 jit_internal_emit_save_all_regs(jit, op);
 if (!(op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0x50 + (op->r_arg[1]); } while (0);
 do { int _imm = (int) (op->r_arg[0]); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 do { *(jit->ip)++ = (unsigned char)0xe8; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((int)(printf)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
 if ((op->code & 0x02)) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((4)) >= -128 && (int)((4)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((4)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((4)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 else do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((8)) >= -128 && (int)((8)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((8)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 jit_internal_emit_restore_all_regs(jit, op);
}
static void jit_internal_emit_trace_op(struct jit *jit, jit_op *op)
{
 int trace = 0;
 jit_internal_emit_save_all_regs(jit, op);
 jit_opcode prev_code = ((jit_opcode) (op->prev->code & 0xfff8));
 jit_opcode next_code = ((jit_opcode) (op->next->code & 0xfff8));
 if ((prev_code == JIT_PROLOG) || (prev_code == JIT_LABEL) || (prev_code == JIT_PATCH)) trace |= (1);
 if ((next_code != JIT_PROLOG) && (next_code != JIT_LABEL) && (next_code != JIT_PATCH)) trace |= (2);
 do { int _imm = (int) (trace); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 do { int _imm = (int) (op->r_arg[0]); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 do { int _imm = (int) (op); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 do { int _imm = (int) (jit); if ((((int)(_imm) >= -128 && (int)(_imm) <= 127))) { *(jit->ip)++ = (unsigned char)0x6A; do { *((jit->ip)) = (unsigned char)(((_imm)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x68; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((_imm)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 do { *(jit->ip)++ = (unsigned char)0xe8; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((int)(jit_trace_callback)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
 do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((16)) >= -128 && (int)((16)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((16)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 jit_internal_emit_restore_all_regs(jit, op);
}
static void jit_internal_emit_fret_op(struct jit * jit, jit_op * op)
{
 jit_value arg = op->r_arg[0];
 do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((arg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 do { *(jit->ip)++ = (1) ? (unsigned char)0xdd : (unsigned char)0xd9; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 jit->push_count -= jit_internal_emit_pop_callee_saved_regs(jit);
 if (jit_current_func_info(jit)->has_prolog) {
  do { switch ((4)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ESP)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EBP); } while (0);
 }
 do { *(jit->ip)++ = (unsigned char)0xc3; } while (0);
}
static void jit_internal_emit_fretval_op(struct jit * jit, jit_op * op)
{
 do { *(jit->ip)++ = (1) ? (unsigned char)0xdd: (unsigned char)0xd9; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((2 + ((1) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((X86_ESP)) == X86_ESP) { if (((-8)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-8)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-8))) >= -128 && (int)(((-8))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-8))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-8))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
}
struct jit_reg_allocator * jit_reg_allocator_create()
{
 int reg = 0;
 struct jit_reg_allocator * a = malloc(sizeof(struct jit_reg_allocator));
 a->gp_reg_cnt = 4;
 a->gp_regs = malloc(sizeof(jit_hw_reg) * (a->gp_reg_cnt + 1));
 a->gp_regs[reg++] = (jit_hw_reg) { X86_EAX, "eax", 0, 0, 5 };
 a->gp_regs[reg++] = (jit_hw_reg) { X86_EBX, "ebx", 1, 0, 0 };
 a->gp_regs[reg++] = (jit_hw_reg) { X86_ECX, "ecx", 0, 0, 3 };
 a->gp_regs[reg++] = (jit_hw_reg) { X86_EDX, "edx", 0, 0, 4 };
 a->gp_regs[reg++] = (jit_hw_reg) { X86_EBP, "ebp", 0, 0, 100 };
 a->gp_arg_reg_cnt = 0;
 a->fp_reg = X86_EBP;
 a->ret_reg = &(a->gp_regs[0]);
 a->fpret_reg = NULL;
 a->fp_reg_cnt = 4;
 reg = 0;
 a->fp_regs = malloc(sizeof(jit_hw_reg) * a->fp_reg_cnt);
 a->fp_regs[reg++] = (jit_hw_reg) { X86_XMM0, "xmm0", 0, 1, 1 };
 a->fp_regs[reg++] = (jit_hw_reg) { X86_XMM1, "xmm1", 0, 1, 2 };
 a->fp_regs[reg++] = (jit_hw_reg) { X86_XMM2, "xmm2", 0, 1, 3 };
 a->fp_regs[reg++] = (jit_hw_reg) { X86_XMM3, "xmm3", 0, 1, 4 };
 a->fp_arg_reg_cnt = 0;
 a->gp_arg_regs = NULL;
 a->fp_arg_regs = NULL;
 return a;
}
static int jit_internal_emit_push_reg(struct jit * jit, jit_hw_reg * r, int stack_offset)
{
 if (!r->fp) {
  stack_offset += (sizeof(void *));
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-stack_offset)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-stack_offset))) >= -128 && (int)(((-stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-stack_offset)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-stack_offset))) >= -128 && (int)(((-stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else {
  stack_offset += 8;
  do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_ESP)) == X86_ESP) { if (((-stack_offset)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-stack_offset))) >= -128 && (int)(((-stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-stack_offset)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-stack_offset))) >= -128 && (int)(((-stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
 return stack_offset;
}
static int jit_internal_emit_pop_reg(struct jit * jit, jit_hw_reg * r, int stack_offset)
{
 if (!r->fp) {
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((stack_offset)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_offset))) >= -128 && (int)(((stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_offset)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((stack_offset))) >= -128 && (int)(((stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  stack_offset += (sizeof(void *));
 } else {
  do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((X86_ESP)) == X86_ESP) { if (((stack_offset)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_offset))) >= -128 && (int)(((stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_offset)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((stack_offset))) >= -128 && (int)(((stack_offset))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_offset))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((r->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_offset))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  stack_offset += 8;
 }
 return stack_offset;
}
static int jit_internal_emit_push_callee_saved_regs(struct jit * jit, jit_op * op)
{
 int stack_offset = 0;
 for (int i = 0; i < jit->reg_al->gp_reg_cnt; i++) {
  jit_hw_reg * r = &(jit->reg_al->gp_regs[i]);
  if (r->callee_saved)
   for (struct jit_op * o = op->next; o != NULL; o = o->next) {
    if (((jit_opcode) (o->code & 0xfff8)) == JIT_PROLOG) break;
    if (jit_internal_uses_hw_reg(o, r->id, 0)) {
     stack_offset = jit_internal_emit_push_reg(jit, r, stack_offset);
     break;
    }
   }
 }
 stack_offset = jit_value_align(stack_offset, (4));
 if (stack_offset) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((stack_offset)) >= -128 && (int)((stack_offset)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((stack_offset)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 return stack_offset / (sizeof(void *));
}
static int jit_internal_emit_pop_callee_saved_regs(struct jit * jit)
{
 int count = 0;
 struct jit_op * op = jit->current_func;
 jit_hw_reg *active_regs[32];
 for (int i = jit->reg_al->gp_reg_cnt - 1; i >= 0; i--) {
  jit_hw_reg * r = &(jit->reg_al->gp_regs[i]);
  if (r->callee_saved)
   for (struct jit_op * o = op->next; o != NULL; o = o->next) {
    if (((jit_opcode) (o->code & 0xfff8)) == JIT_PROLOG) break;
    if (jit_internal_uses_hw_reg(o, r->id, 0)) {
     active_regs[count] = r;
     count++;
     break;
    }
   }
 }
 int stack_space = jit_value_align(count * (sizeof(void *)), (4));
 int stack_offset = stack_space - (count * (sizeof(void *)));
 for (int i = 0; i < count; i++) {
  stack_offset = jit_internal_emit_pop_reg(jit, active_regs[i], stack_offset);
 }
 if (stack_space) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_space)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((stack_space)) >= -128 && (int)((stack_space)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((stack_space)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_space)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 return count;
}
static int jit_internal_generic_push_caller_saved_regs(struct jit * jit, jit_op * op, int reg_count,
  jit_hw_reg * regs, int fp, jit_hw_reg * skip_reg, int stack_offset)
{
 jit_value reg;
 int skip_reg_id = (skip_reg ? skip_reg->id :-1);
 for (int i = 0; i < reg_count; i++) {
  if ((regs[i].id == skip_reg_id) || (regs[i].callee_saved)) continue;
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, regs[i].id, fp, &reg);
  if (hreg && jit_set_get(op->live_in, reg)) {
   stack_offset = jit_internal_emit_push_reg(jit, hreg, stack_offset);
  }
 }
 return stack_offset;
}
static int jit_internal_emit_push_caller_saved_regs(struct jit * jit, jit_op * op)
{
 int stack_offset = 0;
 struct jit_reg_allocator * al = jit->reg_al;
 while (op) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_CALL) break;
  op = op->next;
 }
 stack_offset = jit_internal_generic_push_caller_saved_regs(jit, op, al->gp_reg_cnt, al->gp_regs, 0, al->ret_reg, stack_offset);
 stack_offset = jit_internal_generic_push_caller_saved_regs(jit, op, al->fp_reg_cnt, al->fp_regs, 1, al->fpret_reg, stack_offset);
 if (stack_offset) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((stack_offset)) >= -128 && (int)((stack_offset)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((stack_offset)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 int count = stack_offset / (sizeof(void *));
 return count;
}
static int jit_internal_generic_pop_caller_saved_regs(struct jit * jit, jit_op * op, int reg_count,
  jit_hw_reg * regs, int fp, jit_hw_reg * skip_reg, int stack_offset)
{
 jit_value reg;
 int skip_reg_id = (skip_reg ? skip_reg->id :-1);
 for (int i = reg_count - 1; i >= 0; i--) {
  if ((regs[i].id == skip_reg_id) || (regs[i].callee_saved)) continue;
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, regs[i].id, fp, &reg);
  if (hreg && jit_set_get(op->live_in, reg)) {
   stack_offset = jit_internal_emit_pop_reg(jit, hreg, stack_offset);
  }
 }
 return stack_offset;
}
static int jit_internal_emit_pop_caller_saved_regs(struct jit * jit, jit_op * op)
{
 struct jit_reg_allocator * al = jit->reg_al;
 int stack_offset = 0;
 stack_offset = jit_internal_generic_pop_caller_saved_regs(jit, op, al->fp_reg_cnt, al->fp_regs, 1, al->fpret_reg, stack_offset);
 stack_offset = jit_internal_generic_pop_caller_saved_regs(jit, op, al->gp_reg_cnt, al->gp_regs, 0, al->ret_reg, stack_offset);
 if (stack_offset) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((stack_offset)) >= -128 && (int)((stack_offset)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((stack_offset)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((stack_offset)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 int count = stack_offset / (sizeof(void *));
 return count;
}
static int jit_internal_is_active_register(struct jit_reg_allocator *al, jit_hw_reg *reg, jit_op *op)
{
 if (op->next == NULL) return 0;
 if ((((jit_opcode) (op->next->code & 0xfff8)) == JIT_PUTARG) || (((jit_opcode) (op->next->code & 0xfff8)) == JIT_FPUTARG) || (((jit_opcode) (op->next->code & 0xfff8)) == JIT_CALL)) return 1;
 if ((((jit_opcode) (op->next->code & 0xfff8)) == JIT_RETVAL) && (reg == al->ret_reg)) return 1;
 if (op->next->regmap == NULL) return 1;
 if (op->prev->regmap == NULL) return 1;
 jit_value vreg;
 jit_hw_reg *hw = jit_internal_rmap_is_associated(op->regmap, reg->id, reg->fp, &vreg);
 if (hw) {
  if (op->prev && ((op->prev->live_in && jit_set_get(op->prev->live_in, vreg)) || ((op->prev->live_out && jit_set_get(op->prev->live_out, vreg))))) return 1;
  if (op->next && ((op->next->live_in && jit_set_get(op->next->live_in, vreg)) || ((op->next->live_out && jit_set_get(op->next->live_out, vreg))))) return 1;
  return 0;
 }
 return 0;
}
static int jit_internal_required_stack_space_for_regs(struct jit *jit, jit_op *op)
{
 struct jit_reg_allocator * al = jit->reg_al;
 int space = (sizeof(void *));
 if (!jit_current_func_info(jit)->has_prolog) space += (sizeof(void *));
 for (int i = 0; i < al->gp_reg_cnt; i++) {
  jit_hw_reg *reg = &al->gp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   space += (sizeof(void *));
 }
 for (int i = 0; i < al->fp_reg_cnt; i++) {
  jit_hw_reg *reg = &al->fp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   space += sizeof(double) * 2;
 }
 return space;
}
static void jit_internal_emit_save_all_regs(struct jit *jit, jit_op *op)
{
 struct jit_reg_allocator * al = jit->reg_al;
 do { *(jit->ip)++ = (unsigned char)0x9c; } while (0);
 for (int i = 0; i < al->gp_reg_cnt; i++) {
  jit_hw_reg *reg = &al->gp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   do { *(jit->ip)++ = (unsigned char)0x50 + (reg->id); } while (0);
 }
 for (int i = 0; i < al->fp_reg_cnt; i++) {
  jit_hw_reg *reg = &al->fp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   { do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((8)) >= -128 && (int)((8)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((8)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); } while(0);
 }
 int alignment = jit_internal_required_stack_space_for_regs(jit, op) % 16;
 if (alignment != 0) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16 - alignment)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((16 - alignment)) >= -128 && (int)((16 - alignment)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((16 - alignment)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16 - alignment)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
}
static void jit_internal_emit_restore_all_regs(struct jit *jit, jit_op *op)
{
 int alignment = jit_internal_required_stack_space_for_regs(jit, op) % 16;
 if (alignment != 0) do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16 - alignment)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((16 - alignment)) >= -128 && (int)((16 - alignment)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((16 - alignment)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((16 - alignment)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 struct jit_reg_allocator * al = jit->reg_al;
 for (int i = al->fp_reg_cnt - 1; i >= 0; i--) {
  jit_hw_reg *reg = &al->fp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   { do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((reg->id)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((8)) >= -128 && (int)((8)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((8)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((8)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);} while(0);
 }
 for (int i = al->gp_reg_cnt - 1; i >= 0; i--) {
  jit_hw_reg *reg = &al->gp_regs[i];
  if (!reg->callee_saved && jit_internal_is_active_register(al, reg, op))
   do { *(jit->ip)++ = (unsigned char)0x58 + (reg->id); } while (0);
 }
 do { *(jit->ip)++ = (unsigned char)0x9d; } while (0);
}
static void jit_internal_emit_lreg(struct jit * jit, int hreg_id, jit_value vreg)
{
 int stack_pos = jit_internal_GET_REG_POS(jit, vreg) ;
 if (((vreg) & 0x01) == (1)) do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((X86_EBP)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 else do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((X86_EBP)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
}
static void jit_internal_emit_ureg(struct jit * jit, jit_value vreg, int hreg_id)
{
 int stack_pos = jit_internal_GET_REG_POS(jit, vreg);
 if (((vreg) & 0x01) == (1)) do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x13; do { if (((X86_EBP)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 else do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((X86_EBP)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((hreg_id)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
}
static void jit_internal_emit_get_arg_from_stack(struct jit * jit, int type, int size, int dreg, int stack_reg, int stack_pos)
{
 if (type != JIT_FLOAT_NUM) {
  if (size == (sizeof(void *))) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((stack_reg)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((stack_reg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else if (type == JIT_SIGNED_NUM)
   do { *(jit->ip)++ = (unsigned char)0x0f; switch (size) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert(0); } do { if (((stack_reg)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((stack_reg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x0f; switch (size) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert(0); } do { if (((stack_reg)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((stack_reg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else {
  if (size == sizeof(float)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { if (((stack_reg)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((stack_reg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x12; do { if (((stack_reg)) == X86_ESP) { if (((stack_pos)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((stack_pos)) == 0 && ((stack_reg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); break; } if ((((int)(((stack_pos))) >= -128 && (int)(((stack_pos))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((stack_pos))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((stack_reg)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((stack_pos))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
}
static void jit_internal_emit_get_arg(struct jit * jit, jit_op * op)
{
 struct jit_func_info * info = jit_current_func_info(jit);
 int dreg = op->r_arg[0];
 int arg_id = op->r_arg[1];
 struct jit_inp_arg * arg = &(info->args[arg_id]);
 int size = arg->size;
 int type = arg->type;
 int reg_id = (((type == JIT_FLOAT_NUM ? (1) : (0)) & 0x01) | ((((3)) & 0x03) << 1) | ((arg_id) & 0xfffffff) << 4);
 int read_from_stack = 0;
 int stack_pos;
 if (!arg->passed_by_reg) {
  read_from_stack = 1;
  stack_pos = arg->location.stack_pos;
  if (!jit_current_func_info(jit)->has_prolog) {
   stack_pos -= (sizeof(void *));
   stack_pos += jit->push_count * (sizeof(void *));
   jit_internal_emit_get_arg_from_stack(jit, type, size, dreg, X86_ESP, stack_pos);
   return;
  }
 }
 if (arg->passed_by_reg && jit_internal_rmap_get(op->regmap, reg_id) == NULL) {
  read_from_stack = 1;
  stack_pos = arg->spill_pos;
 }
 if (read_from_stack) {
  jit_internal_emit_get_arg_from_stack(jit, type, size, dreg, X86_EBP, stack_pos);
  return;
 }
 jit_hw_reg *arg_reg = jit_internal_rmap_get(op->regmap, reg_id);
 if (type != JIT_FLOAT_NUM) {
  if (size == (sizeof(void *))) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((arg_reg->id)))&0x07))); } while (0); } while (0); } while (0);
  else if (type == JIT_SIGNED_NUM) do { *(jit->ip)++ = (unsigned char)0x0f; switch ((size)) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((arg_reg->id)))&0x07))); } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x0f; switch ((size)) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((arg_reg->id)))&0x07))); } while (0); } while (0); } while (0);
 } else {
  if (size == sizeof(float)) do { *(jit->ip)++ = (unsigned char)0xf3; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x5a; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dreg)))&0x07)<<3)|(((((arg_reg->id)))&0x07))); } while (0); } while (0); } while (0);
  else do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((arg_reg->id)))&0x07)<<3)|(((((dreg)))&0x07))); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_alu_op(struct jit * jit, struct jit_op * op, int x86_op, int imm)
{
 if (imm) {
  if (op->r_arg[0] != op->r_arg[1]) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { if ((op->r_arg[0]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((x86_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((x86_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 } else {
  if (op->r_arg[0] == op->r_arg[1]) {
   do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
  } else if (op->r_arg[0] == op->r_arg[2]) {
   do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  } else {
   do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
   do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
  }
 }
}
static void jit_internal_emit_sub_op(struct jit * jit, struct jit_op * op, int imm)
{
 if (imm) {
  if (op->r_arg[0] != op->r_arg[1]) do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((op->r_arg[1])) == X86_ESP) { if (((-op->r_arg[2])) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-op->r_arg[2]))) >= -128 && (int)(((-op->r_arg[2]))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-op->r_arg[2]))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-op->r_arg[2]))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-op->r_arg[2])) == 0 && ((op->r_arg[1])) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); break; } if ((((int)(((-op->r_arg[2]))) >= -128 && (int)(((-op->r_arg[2]))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-op->r_arg[2]))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-op->r_arg[2]))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { if ((op->r_arg[0]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
  return;
 }
 if (op->r_arg[0] == op->r_arg[1]) {
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 } else if (op->r_arg[0] == op->r_arg[2]) {
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((3))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
 } else {
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_subx_op(struct jit * jit, struct jit_op * op, int x86_op, int imm)
{
 if (imm) {
  if (op->r_arg[0] != op->r_arg[1]) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { if ((op->r_arg[0]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((x86_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((x86_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
  return;
 }
 if (op->r_arg[0] == op->r_arg[1]) {
  do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 } else if (op->r_arg[0] == op->r_arg[2]) {
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)))) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)))) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else {
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (((unsigned char)(x86_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_rsb_op(struct jit * jit, struct jit_op * op, int imm)
{
 if (imm) {
  if (op->r_arg[0] == op->r_arg[1]) do { if ((op->r_arg[0]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((-op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((-op->r_arg[2])) >= -128 && (int)((-op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((-op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((-op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
  else do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((op->r_arg[1])) == X86_ESP) { if (((-op->r_arg[2])) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-op->r_arg[2]))) >= -128 && (int)(((-op->r_arg[2]))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-op->r_arg[2]))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-op->r_arg[2]))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-op->r_arg[2])) == 0 && ((op->r_arg[1])) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); break; } if ((((int)(((-op->r_arg[2]))) >= -128 && (int)(((-op->r_arg[2]))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-op->r_arg[2]))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-op->r_arg[2]))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((3))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
  return;
 }
 if (op->r_arg[0] == op->r_arg[1]) {
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((3))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
 } else if (op->r_arg[0] == op->r_arg[2]) {
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
 } else {
  do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_mul_op(struct jit * jit, struct jit_op * op, int imm, int sign, int high_bytes)
{
 jit_value dest = op->r_arg[0];
 jit_value factor1 = op->r_arg[1];
 jit_value factor2 = op->r_arg[2];
 if ((!high_bytes) && (imm)) {
  switch (factor2) {
   case 2: if (factor1 == dest) do { if ((1) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((1)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
    else do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((factor1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((factor1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((factor1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    return;
   case 3: do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((factor1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((1)))&0x03)<<6)|(((((factor1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((factor1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((1)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((1)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((1)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); return;
   case 4: if (factor1 != dest) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((factor1)))&0x07))); } while (0); } while (0); } while (0);
    do { if ((2) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((2)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
    return;
   case 5: do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((factor1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((2)))&0x03)<<6)|(((((factor1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((factor1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((2)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((2)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((2)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    return;
   case 8: if (factor1 != dest) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((factor1)))&0x07))); } while (0); } while (0); } while (0);
    do { if ((3) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((3)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
    return;
   case 9: do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((factor1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((3)))&0x03)<<6)|(((((factor1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((factor1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((3)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((3)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((3)))&0x03)<<6)|(((((factor1))&0x7)&0x07)<<3)|((((((factor1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    return;
  }
 }
 int ax_in_use = jit_reg_in_use(op, X86_EAX, 0);
 int dx_in_use = jit_reg_in_use(op, X86_EDX, 0);
 if ((dest != X86_EAX) && ax_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EAX); } while (0);
 if ((dest != X86_EDX) && dx_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EDX); } while (0);
 if (imm) {
  if (factor1 != X86_EAX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EAX)))&0x07)<<3)|(((((factor1)))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xb8 + (X86_EDX); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((factor2)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((4 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((X86_EDX)))&0x07))); } while (0); } while (0); } while (0);
 } else {
  if (factor1 == X86_EAX) do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((4 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((factor2)))&0x07))); } while (0); } while (0); } while (0);
  else if (factor2 == X86_EAX) do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((4 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((factor1)))&0x07))); } while (0); } while (0); } while (0);
  else {
   do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EAX)))&0x07)<<3)|(((((factor1)))&0x07))); } while (0); } while (0); } while (0);
   do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((4 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((factor2)))&0x07))); } while (0); } while (0); } while (0);
  }
 }
 if (!high_bytes) {
  if (dest != X86_EAX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((X86_EAX)))&0x07))); } while (0); } while (0); } while (0);
 } else {
  if (dest != X86_EDX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((X86_EDX)))&0x07))); } while (0); } while (0); } while (0);
 }
 if ((dest != X86_EDX) && dx_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EDX); } while (0);
 if ((dest != X86_EAX) && ax_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EAX); } while (0);
}
static void jit_internal_emit_div_op(struct jit * jit, struct jit_op * op, int imm, int sign, int modulo)
{
 jit_value dest = op->r_arg[0];
 jit_value dividend = op->r_arg[1];
 jit_value divisor = op->r_arg[2];
 if (imm && ((divisor == 2) || (divisor == 4) || (divisor == 8))) {
  if (dest != dividend) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((dividend)))&0x07))); } while (0); } while (0); } while (0);
  if (!modulo) {
   switch (divisor) {
    case 2: do { if ((1) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((1)) & 0xff); ++((jit->ip)); } while (0); } } while (0); break;
    case 4: do { if ((2) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((2)) & 0xff); ++((jit->ip)); } while (0); } } while (0); break;
    case 8: do { if ((3) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((sign ? X86_SAR : X86_SHR)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((3)) & 0xff); ++((jit->ip)); } while (0); } } while (0); break;
   }
   return;
  }
  if (modulo && !sign) {
   switch (divisor) {
    case 2: do { if ((dest) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_AND)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x1)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((0x1)) >= -128 && (int)((0x1)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((0x1)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x1)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
    case 4: do { if ((dest) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_AND)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x3)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((0x3)) >= -128 && (int)((0x3)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((0x3)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x3)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
    case 8: do { if ((dest) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_AND)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x7)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((0x7)) >= -128 && (int)((0x7)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((0x7)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_AND)))&0x07)<<3)|(((((dest)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0x7)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
   }
   return;
  }
 }
 int ax_in_use = jit_reg_in_use(op, X86_EAX, 0);
 int dx_in_use = jit_reg_in_use(op, X86_EDX, 0);
 if ((dest != X86_EAX) && ax_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EAX); } while (0);
 if ((dest != X86_EDX) && dx_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EDX); } while (0);
 if (imm) {
  if (dividend != X86_EAX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EAX)))&0x07)<<3)|(((((dividend)))&0x07))); } while (0); } while (0); } while (0);
  if (sign) do { *(jit->ip)++ = (unsigned char)0x99; } while (0);
  else do { *(jit->ip)++ = (((unsigned char)(X86_XOR)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EDX)))&0x07)<<3)|(((((X86_EDX)))&0x07))); } while (0); } while (0); } while (0);
  if (dest != X86_EBX) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_EBX); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xb8 + (X86_EBX); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((divisor)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((X86_EBX)))&0x07))); } while (0); } while (0); } while (0);
  if (dest != X86_EBX) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EBX); } while (0);
 } else {
  if ((divisor == X86_EAX) || (divisor == X86_EDX)) {
   do { *(jit->ip)++ = (unsigned char)0x50 + (divisor); } while (0);
  }
  if (dividend != X86_EAX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EAX)))&0x07)<<3)|(((((dividend)))&0x07))); } while (0); } while (0); } while (0);
  if (sign) do { *(jit->ip)++ = (unsigned char)0x99; } while (0);
  else do { *(jit->ip)++ = (((unsigned char)(X86_XOR)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EDX)))&0x07)<<3)|(((((X86_EDX)))&0x07))); } while (0); } while (0); } while (0);
  if ((divisor == X86_EAX) || (divisor == X86_EDX)) {
   do { *(jit->ip)++ = (unsigned char)0xf7; do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
   do { if ((X86_ESP) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_ADD)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) (((sizeof(void *)))); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)(((sizeof(void *)))) >= -128 && (int)(((sizeof(void *)))) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)((((sizeof(void *)))) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ADD)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((sizeof(void *)))); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
  } else {
   do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((6 + ((sign) ? 1 : 0)))&0x07)<<3)|(((((divisor)))&0x07))); } while (0); } while (0); } while (0);
  }
 }
 if (!modulo) {
  if (dest != X86_EAX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((X86_EAX)))&0x07))); } while (0); } while (0); } while (0);
 } else {
  if (dest != X86_EDX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((dest)))&0x07)<<3)|(((((X86_EDX)))&0x07))); } while (0); } while (0); } while (0);
 }
 if ((dest != X86_EDX) && dx_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EDX); } while (0);
 if ((dest != X86_EAX) && ax_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EAX); } while (0);
}
static void jit_internal_emit_shift_op(struct jit * jit, struct jit_op * op, int shift_op, int imm)
{
 if (imm) {
  if (op->r_arg[0] != op->r_arg[1]) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
  do { if ((op->r_arg[2]) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((shift_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((shift_op)))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } } while (0);
 } else {
  int destreg = op->r_arg[0];
  int valreg = op->r_arg[1];
  int shiftreg = op->r_arg[2];
  if (destreg != X86_ECX) {
   int cx_in_use = jit_reg_in_use(op, X86_ECX, 0);
   if (cx_in_use && (shiftreg != X86_ECX)) do { *(jit->ip)++ = (unsigned char)0x50 + (X86_ECX); } while (0);
   if (shiftreg != X86_ECX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ECX)))&0x07)<<3)|(((((shiftreg)))&0x07))); } while (0); } while (0); } while (0);
   if (destreg != valreg) {
    if (valreg != X86_ECX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((((valreg)))&0x07))); } while (0); } while (0); } while (0);
    else do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
   }
   do { *(jit->ip)++ = (unsigned char)0xd3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((shift_op)))&0x07)<<3)|(((((destreg)))&0x07))); } while (0); } while (0); } while (0);
   if (cx_in_use && (shiftreg != X86_ECX)) do { *(jit->ip)++ = (unsigned char)0x58 + (X86_ECX); } while (0);
  } else {
   jit_hw_reg * tmp = jit_get_unused_reg(jit->reg_al, op, 0);
   int tmpreg = (tmp ? tmp->id : X86_EAX);
   int tmp_in_use = jit_reg_in_use(op, tmpreg, 0);
   if (tmp_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (tmpreg); } while (0);
   if (tmpreg != valreg) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((tmpreg)))&0x07)<<3)|(((((valreg)))&0x07))); } while (0); } while (0); } while (0);
   if (shiftreg != X86_ECX) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ECX)))&0x07)<<3)|(((((shiftreg)))&0x07))); } while (0); } while (0); } while (0);
   do { *(jit->ip)++ = (unsigned char)0xd3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((shift_op)))&0x07)<<3)|(((((tmpreg)))&0x07))); } while (0); } while (0); } while (0);
   do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((destreg)))&0x07)<<3)|(((((tmpreg)))&0x07))); } while (0); } while (0); } while (0);
   if (tmp_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (tmpreg); } while (0);
  }
 }
}
static void jit_internal_emit_cond_op(struct jit * jit, struct jit_op * op, int amd64_cond, int imm, int sign)
{
 if (imm) do { if ((op->r_arg[1]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_CMP)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_CMP)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_CMP)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 else do { *(jit->ip)++ = (((unsigned char)(X86_CMP)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[1])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 if ((op->r_arg[0] != X86_ESI) && (op->r_arg[0] != X86_EDI)) {
  do { *(jit->ip)++ = (unsigned char)0xb8 + (op->r_arg[0]); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
  do { assert(((op->r_arg[0]) < 4)); *(jit->ip)++ = (unsigned char)0x0f; if ((sign)) *(jit->ip)++ = jit_internal_x86_cc_signed_map [(amd64_cond)] + 0x20; else *(jit->ip)++ = jit_internal_x86_cc_unsigned_map [(amd64_cond)] + 0x20; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((0))&0x07)<<3)|(((((op->r_arg[0])))&0x07))); } while (0); } while (0); } while (0);
 } else {
  do { if (((sizeof(void *))) == 1) *(jit->ip)++ = (unsigned char)0x86; else *(jit->ip)++ = (unsigned char)0x87; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_EAX)))&0x07))); } while (0); } while (0); } while (0);
  do { *(jit->ip)++ = (unsigned char)0xb8 + (X86_EAX); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
  do { assert(((X86_EAX) < 4)); *(jit->ip)++ = (unsigned char)0x0f; if ((sign)) *(jit->ip)++ = jit_internal_x86_cc_signed_map [(amd64_cond)] + 0x20; else *(jit->ip)++ = jit_internal_x86_cc_unsigned_map [(amd64_cond)] + 0x20; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((0))&0x07)<<3)|(((((X86_EAX)))&0x07))); } while (0); } while (0); } while (0);
  do { if (((sizeof(void *))) == 1) *(jit->ip)++ = (unsigned char)0x86; else *(jit->ip)++ = (unsigned char)0x87; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[0])))&0x07)<<3)|(((((X86_EAX)))&0x07))); } while (0); } while (0); } while (0);
 }
}
static void jit_internal_emit_branch_op(struct jit * jit, struct jit_op * op, int cond, int imm, int sign)
{
 if (imm) do { if ((op->r_arg[1]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_CMP)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_CMP)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_CMP)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 else do { *(jit->ip)++ = (((unsigned char)(X86_CMP)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[1])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 do { int offset = ((!jit_is_label(jit, (void *)(op->r_arg[0])) ? (op->r_arg[0]) : (((jit_value)jit->buf + ((jit_label *)(op->r_arg[0]))->pos - (jit_value)jit->ip)))) - 6; do { *((jit->ip))++ = (unsigned char)0x0f; if (((sign))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((cond))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((cond))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
}
static void jit_internal_emit_branch_mask_op(struct jit * jit, struct jit_op * op, int cond, int imm)
{
 if (imm) do { if ((op->r_arg[1]) == X86_EAX) { *(jit->ip)++ = (unsigned char)0xa9; } else { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((0))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
 else do { *(jit->ip)++ = (unsigned char)0x85; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[2])))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 do { int offset = ((!jit_is_label(jit, (void *)(op->r_arg[0])) ? (op->r_arg[0]) : (((jit_value)jit->buf + ((jit_label *)(op->r_arg[0]))->pos - (jit_value)jit->ip)))) - 6; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((cond))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((cond))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
}
static void jit_internal_emit_branch_overflow_op(struct jit * jit, struct jit_op * op, int alu_op, int imm, int negation)
{
 if (imm) do { if ((op->r_arg[1]) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((op->r_arg[2])) >= -128 && (int)((op->r_arg[2])) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((alu_op)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((op->r_arg[2])) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((alu_op)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((op->r_arg[2])); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 else do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((op->r_arg[1])))&0x07)<<3)|(((((op->r_arg[2])))&0x07))); } while (0); } while (0); } while (0);
 op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
 if (!negation) do { int offset = ((!jit_is_label(jit, (void *)(op->r_arg[0])) ? (op->r_arg[0]) : (((jit_value)jit->buf + ((jit_label *)(op->r_arg[0]))->pos - (jit_value)jit->ip)))) - 6; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_O))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_O))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
 else do { int offset = ((!jit_is_label(jit, (void *)(op->r_arg[0])) ? (op->r_arg[0]) : (((jit_value)jit->buf + ((jit_label *)(op->r_arg[0]))->pos - (jit_value)jit->ip)))) - 6; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_NO))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_NO))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
}
static int jit_internal_is_spilled(jit_value arg_id, jit_op * prepare_op, int * reg)
{
        jit_hw_reg * hreg = jit_internal_rmap_get(prepare_op->regmap, arg_id);
        if (hreg) {
                *reg = hreg->id;
                return 0;
        } else return 1;
}
static void jit_internal_emit_ld_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2)
{
 if (op->arg_size == (sizeof(void *))) {
  if ((op->code & 0x02)) do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
  else do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((a2)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  return;
 }
 switch (op->code) {
  case (JIT_LD | 0x02 | 0x00): do { *(jit->ip)++ = (unsigned char)0x0f; switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0); break;
  case (JIT_LD | 0x02 | 0x04): do { *(jit->ip)++ = (unsigned char)0x0f; switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0); break;
  case (JIT_LD | 0x01 | 0x00): do { *(jit->ip)++ = (unsigned char)0x0f; switch (op->arg_size) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert(0); } do { if (((a2)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_LD | 0x01 | 0x04): do { *(jit->ip)++ = (unsigned char)0x0f; switch (op->arg_size) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert(0); } do { if (((a2)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  default: assert(0);
 }
}
static void jit_internal_emit_ldx_op(struct jit * jit, jit_op * op, jit_value a1, jit_value a2, jit_value a3)
{
 if (op->arg_size == (sizeof(void *))) {
  if ((op->code & 0x02)) do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  else do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  return;
 }
 switch (op->code) {
  case (JIT_LDX | 0x02 | 0x00): do { *(jit->ip)++ = (unsigned char)0x0f; switch (op->arg_size) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert(0); } do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_LDX | 0x02 | 0x04): do { *(jit->ip)++ = (unsigned char)0x0f; switch (op->arg_size) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert(0); } do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_LDX | 0x01 | 0x00): do { *(jit->ip)++ = (unsigned char)0x0f; switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert (0); } do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_LDX | 0x01 | 0x04): do { *(jit->ip)++ = (unsigned char)0x0f; switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0xb6; break; case 2: *(jit->ip)++ = (unsigned char)0xb7; break; default: assert (0); } do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  default: assert(0);
 }
}
struct transfer_info {
 int sourcereg;
 int destreg;
 int scrapreg;
 int scrap_in_use;
 int counterreg;
 int counter_in_use;
 int block_size;
 unsigned char *loop_addr;
};
static void jit_internal_emit_transfer_init(struct jit * jit, jit_op * op, jit_value destreg, jit_value srcreg, jit_value cnt, int block_size)
{
 struct transfer_info *tinf = malloc(sizeof(struct transfer_info));
 tinf->sourcereg = srcreg;
 tinf->destreg = destreg;
 tinf->block_size = block_size;
 jit_hw_reg * scrap = jit_get_unused_reg_with_index(jit->reg_al, op, 0, 0);
 if (scrap) tinf->scrapreg = scrap->id;
 else {
  for (int i = 0; i < jit->reg_al->gp_reg_cnt; i++) {
   jit_hw_reg *r = &jit->reg_al->gp_regs[i];
   if ((r->id != srcreg) && (r->id != destreg) && (!(op->code & 0x02) && (r->id != cnt))) {
    tinf->scrapreg = r->id;
    break;
   }
  }
 }
 tinf->scrap_in_use = jit_reg_in_use(op, tinf->scrapreg, 0);
 if ((op->code & 0x02)) {
  jit_hw_reg * counter = jit_get_unused_reg_with_index(jit->reg_al, op, 0, 1);
  if (counter) tinf->counterreg = counter->id;
  else {
   for (int i = 0; i < jit->reg_al->gp_reg_cnt; i++) {
    jit_hw_reg *r = &jit->reg_al->gp_regs[i];
    if ((r->id != srcreg) && (r->id != destreg) && (r->id != tinf->scrapreg)) {
     tinf->counterreg = r->id;
     break;
    }
   }
  }
  tinf->counter_in_use = jit_reg_in_use(op, tinf->counterreg, 0);
 } else {
  if (jit_set_get(op->live_out, op->arg[2])) {
   jit_hw_reg * counter = jit_get_unused_reg_with_index(jit->reg_al, op, 0, 1);
   tinf->counterreg = (counter ? counter->id : cnt);
   tinf->counter_in_use = jit_reg_in_use(op, tinf->counterreg, 0);
  } else {
   tinf->counterreg = cnt;
   tinf->counter_in_use = 0;
  }
 }
 if (tinf->counter_in_use) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)))) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 if (tinf->scrap_in_use) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)) * 2)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)) * 2)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 if ((op->code & 0x02)) do { *(jit->ip)++ = (unsigned char)0xb8 + (tinf->counterreg); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((cnt * block_size)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
 else if ((tinf->counterreg != cnt) || block_size > 1) {
  int shift;
  if (block_size == 1) shift = 0;
  else if (block_size == 2) shift = 1;
  else if (block_size == 4) shift = 2;
  else if (block_size == 8) shift = 3;
  else assert(0);
  do { *(jit->ip)++ = (unsigned char)0x8d; do { if ((((-1))) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((shift)))&0x03)<<6)|(((((cnt)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && (((-1))) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((shift)))&0x03)<<6)|(((((cnt))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((shift)))&0x03)<<6)|(((((cnt))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((shift)))&0x03)<<6)|(((((cnt))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 }
 tinf->loop_addr = jit->ip;
 op->addendum = tinf;
 if (block_size == (sizeof(void *))) do { switch ((block_size)) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((srcreg)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((srcreg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 else do { *(jit->ip)++ = (unsigned char)0x0f; switch ((block_size)) { case 1: *(jit->ip)++ = (unsigned char)0xbe; break; case 2: *(jit->ip)++ = (unsigned char)0xbf; break; default: assert (0); } do { if (((srcreg)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((srcreg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((srcreg))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
}
static void jit_internal_emit_transfer_loop(struct jit *jit, jit_op *op)
{
 struct transfer_info *tinf = (struct transfer_info *)op->addendum;
 jit_value loop = (jit_value) tinf->loop_addr;
 do { switch ((tinf->block_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((tinf->destreg)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-tinf->block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-tinf->block_size)) == 0 && ((tinf->destreg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); } else if ((((int)(((-tinf->block_size))) >= -128 && (int)(((-tinf->block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-tinf->block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-tinf->block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 do { if ((tinf->counterreg) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((tinf->block_size)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((tinf->block_size)) >= -128 && (int)((tinf->block_size)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((tinf->counterreg)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((tinf->block_size)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((tinf->counterreg)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((tinf->block_size)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 do { int offset = (loop - (jit_value) jit->ip) - 2; if ((((int)((offset)) >= -128 && (int)((offset)) <= 127))) do { if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_NZ))]; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_NZ))]; do { *(((jit->ip))) = (unsigned char)(((offset)) & 0xff); ++(((jit->ip))); } while (0); } while (0); else { offset -= 4; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_NZ))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_NZ))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } } while (0);
 if (tinf->counter_in_use) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)))) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 if (tinf->scrap_in_use) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)) * 2)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)) * 2)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
}
static void jit_internal_emit_transfer_op(struct jit *jit, jit_op *op, int alu_op)
{
 jit_op *init_op = op->prev;
 while (((jit_opcode) (init_op->code & 0xfff8)) != JIT_TRANSFER)
  init_op = init_op->prev;
 struct transfer_info *tinf = (struct transfer_info *)init_op->addendum;
 if (op->arg[1] == (((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((1) & 0xfffffff) << 4))) {
  do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { if (((tinf->destreg)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-tinf->block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-tinf->block_size)) == 0 && ((tinf->destreg)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); } else if ((((int)(((-tinf->block_size))) >= -128 && (int)(((-tinf->block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-tinf->block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((tinf->counterreg))&0x7)&0x07)<<3)|((((((tinf->destreg))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-tinf->block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 } else if (op->r_arg[1] != -1) {
  if ((op->r_arg[1] == tinf->counterreg) && (tinf->counter_in_use)) {
   do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)))) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *))))) >= -128 && (int)(((-(sizeof(void *))))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *))))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *))))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  } else if ((op->r_arg[1] == tinf->scrapreg) && (tinf->scrap_in_use)) {
   do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { if (((X86_ESP)) == X86_ESP) { if (((-(sizeof(void *)) * 2)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((-(sizeof(void *)) * 2)) == 0 && ((X86_ESP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); break; } if ((((int)(((-(sizeof(void *)) * 2))) >= -128 && (int)(((-(sizeof(void *)) * 2))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-(sizeof(void *)) * 2))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_ESP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-(sizeof(void *)) * 2))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
  } else do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((op->r_arg[1])))&0x07))); } while (0); } while (0); } while (0);
 }
 else do { *(jit->ip)++ = (((unsigned char)(alu_op)) << 3) + 3; do { if (((X86_EBP)) == X86_ESP) { if (((jit_internal_GET_REG_POS(jit, op->arg[1]))) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((jit_internal_GET_REG_POS(jit, op->arg[1])))) >= -128 && (int)(((jit_internal_GET_REG_POS(jit, op->arg[1])))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((jit_internal_GET_REG_POS(jit, op->arg[1])))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((jit_internal_GET_REG_POS(jit, op->arg[1])))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((jit_internal_GET_REG_POS(jit, op->arg[1]))) == 0 && ((X86_EBP)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); break; } if ((((int)(((jit_internal_GET_REG_POS(jit, op->arg[1])))) >= -128 && (int)(((jit_internal_GET_REG_POS(jit, op->arg[1])))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((jit_internal_GET_REG_POS(jit, op->arg[1])))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((tinf->scrapreg)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((jit_internal_GET_REG_POS(jit, op->arg[1])))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 if (op->arg[0]) jit_internal_emit_transfer_loop(jit, (jit_op *)op->arg[0]);
}
static void jit_internal_emit_memcpy(struct jit * jit, jit_op * op, jit_value a1, jit_value a2, jit_value a3)
{
 jit_internal_emit_transfer_init(jit, op, a1, a2, a3, 1);
 jit_internal_emit_transfer_loop(jit, op);
}
static void jit_internal_emit_memset(struct jit *jit, jit_op *op, jit_value a1, jit_value a2, jit_value a3, int block_size)
{
 jit_hw_reg * counter = jit_get_unused_reg_with_index(jit->reg_al, op, 0, 0);
 int counterreg = 0;
 if (counter) counterreg = counter->id;
 else {
  for (int i = 0; i < jit->reg_al->gp_reg_cnt; i++) {
   jit_hw_reg *r = &jit->reg_al->gp_regs[i];
   if ((r->id != a1) && (r->id != a2) && (!(op->code & 0x02) && (r->id != a3))) {
    counterreg = r->id;
    break;
   }
  }
 }
        int counter_in_use = jit_reg_in_use(op, counterreg, 0);
 if (counter_in_use) do { *(jit->ip)++ = (unsigned char)0x50 + (counterreg); } while (0);
 do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((counterreg)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
 if (block_size == 2) do { if ((1) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((1)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
 if (block_size == 4) do { if ((2) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((2)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
 if (block_size == 8) do { if ((3) == 1) { *(jit->ip)++ = (unsigned char)0xd1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); } else { *(jit->ip)++ = (unsigned char)0xc1; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SHL)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((3)) & 0xff); ++((jit->ip)); } while (0); } } while (0);
 jit_value loop = (jit_value) jit->ip;
 if ((op->code & 0x02))
  do { if ((block_size) == 1) { *(jit->ip)++ = (unsigned char)0xc6; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *((jit->ip)) = (unsigned char)(((a3)) & 0xff); ++((jit->ip)); } while (0); } else if ((block_size) == 2) { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *(short*)((jit->ip)) = ((a3)); ((jit->ip)) += 2; } while (0); } else { *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a3)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 else
  do { switch ((block_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((-block_size)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((-block_size))) >= -128 && (int)(((-block_size))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((-block_size))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((counterreg))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((-block_size))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
 do { if ((counterreg) == X86_EAX) { *(jit->ip)++ = (((unsigned char)(X86_SUB)) << 3) + 5; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((block_size)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); break; } if ((((int)((block_size)) >= -128 && (int)((block_size)) <= 127))) { *(jit->ip)++ = (unsigned char)0x83; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((block_size)) & 0xff); ++((jit->ip)); } while (0); } else { *(jit->ip)++ = (unsigned char)0x81; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_SUB)))&0x07)<<3)|(((((counterreg)))&0x07))); } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((block_size)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0);
 do { int offset = (loop - (jit_value) jit->ip) - 2; if ((((int)((offset)) >= -128 && (int)((offset)) <= 127))) do { if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_NZ))]; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_NZ))]; do { *(((jit->ip))) = (unsigned char)(((offset)) & 0xff); ++(((jit->ip))); } while (0); } while (0); else { offset -= 4; do { *((jit->ip))++ = (unsigned char)0x0f; if (((0))) *((jit->ip))++ = jit_internal_x86_cc_signed_map [((jit_internal_X86_CC_NZ))] + 0x10; else *((jit->ip))++ = jit_internal_x86_cc_unsigned_map [((jit_internal_X86_CC_NZ))] + 0x10; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((offset)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } } while (0);
 if (counter_in_use) do { *(jit->ip)++ = (unsigned char)0x58 + (counterreg); } while (0);
}
int jit_allocai(struct jit * jit, int size)
{
 jit_value real_size = jit_value_align(size, (4));
 jit_add_op(jit, JIT_ALLOCA | 0x02, (((0x00) << 4) | ((0x00) << 2) | (0x02)), real_size, 0, 0, 0, NULL);
 jit_current_func_info(jit)->allocai_mem += real_size;
 return -(jit_current_func_info(jit)->allocai_mem);
}
void jit_patch_local_addrs(struct jit *jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_REF_DATA)) {
   unsigned char *buf = jit->buf + (long) op->patch_addr;
   jit_value addr = jit_is_label(jit, (void *)op->arg[1]) ? ((jit_label *)op->arg[1])->pos : op->arg[1];
   do { *(buf)++ = (unsigned char)0xb8 + (op->r_arg[0]); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((jit->buf + addr)); *((buf))++ = imb.b [0]; *((buf))++ = imb.b [1]; *((buf))++ = imb.b [2]; *((buf))++ = imb.b [3]; } while (0); } while (0);
  }
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_DATA)) {
   unsigned char *buf = jit->buf + (long) op->patch_addr;
   jit_value addr = jit_is_label(jit, (void *)op->arg[0]) ? ((jit_label *)op->arg[0])->pos : op->arg[0];
   *((jit_value *)buf) = (jit_value) (jit->buf + addr);
  }
 }
}
void jit_gen_op(struct jit * jit, struct jit_op * op)
{
 jit_value a1 = op->r_arg[0];
 jit_value a2 = op->r_arg[1];
 jit_value a3 = op->r_arg[2];
 int imm = (op->code & 0x02);
 int sign = (!(op->code & 0x04));
 int found = 1;
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_ADD:
   if ((a1 != a2) && (a1 != a3)) {
    if (imm) do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((a2)) == X86_ESP) { if (((a3)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a3)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
    else do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0);
   } else jit_internal_emit_alu_op(jit, op, X86_ADD, imm);
   break;
  case JIT_ADDC: jit_internal_emit_alu_op(jit, op, X86_ADD, imm); break;
  case JIT_ADDX: jit_internal_emit_alu_op(jit, op, X86_ADC, imm); break;
  case JIT_SUB: jit_internal_emit_sub_op(jit, op, imm); break;
  case JIT_SUBC: jit_internal_emit_subx_op(jit, op, X86_SUB, imm); break;
  case JIT_SUBX: jit_internal_emit_subx_op(jit, op, X86_SBB, imm); break;
  case JIT_RSB: jit_internal_emit_rsb_op(jit, op, imm); break;
  case JIT_NEG:
    if (a1 != a2) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
    do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((3))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
    break;
  case JIT_OR: jit_internal_emit_alu_op(jit, op, X86_OR, imm); break;
  case JIT_XOR: jit_internal_emit_alu_op(jit, op, X86_XOR, imm); break;
  case JIT_AND: jit_internal_emit_alu_op(jit, op, X86_AND, imm); break;
  case JIT_NOT: if (a1 != a2) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0);
          do { *(jit->ip)++ = (unsigned char)0xf7; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((2))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
          break;
  case JIT_LSH: jit_internal_emit_shift_op(jit, op, X86_SHL, imm); break;
  case JIT_RSH: jit_internal_emit_shift_op(jit, op, sign ? X86_SAR : X86_SHR, imm); break;
  case JIT_LT: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_LT, imm, sign); break;
  case JIT_LE: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_LE, imm, sign); break;
  case JIT_GT: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_GT, imm, sign); break;
  case JIT_GE: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_GE, imm, sign); break;
  case JIT_EQ: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_EQ, imm, sign); break;
  case JIT_NE: jit_internal_emit_cond_op(jit, op, jit_internal_X86_CC_NE, imm, sign); break;
  case JIT_BLT: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_LT, imm, sign); break;
  case JIT_BLE: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_LE, imm, sign); break;
  case JIT_BGT: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_GT, imm, sign); break;
  case JIT_BGE: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_GE, imm, sign); break;
  case JIT_BEQ: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_EQ, imm, sign); break;
  case JIT_BNE: jit_internal_emit_branch_op(jit, op, jit_internal_X86_CC_NE, imm, sign); break;
  case JIT_BMS: jit_internal_emit_branch_mask_op(jit, op, jit_internal_X86_CC_NZ, imm); break;
  case JIT_BMC: jit_internal_emit_branch_mask_op(jit, op, jit_internal_X86_CC_Z, imm); break;
  case JIT_BOADD: jit_internal_emit_branch_overflow_op(jit, op, X86_ADD, imm, 0); break;
  case JIT_BOSUB: jit_internal_emit_branch_overflow_op(jit, op, X86_SUB, imm, 0); break;
  case JIT_BNOADD: jit_internal_emit_branch_overflow_op(jit, op, X86_ADD, imm, 1); break;
  case JIT_BNOSUB: jit_internal_emit_branch_overflow_op(jit, op, X86_SUB, imm, 1); break;
  case JIT_MUL: jit_internal_emit_mul_op(jit, op, imm, sign, 0); break;
  case JIT_HMUL: jit_internal_emit_mul_op(jit, op, imm, sign, 1); break;
  case JIT_DIV: jit_internal_emit_div_op(jit, op, imm, sign, 0); break;
  case JIT_MOD: jit_internal_emit_div_op(jit, op, imm, sign, 1); break;
  case JIT_CALL: jit_internal_emit_funcall(jit, op, imm); break;
  case JIT_PATCH: do {
     struct jit_op *target = (struct jit_op *) a1;
     if (!target->in_use) break;
     switch (((jit_opcode) (target->code & 0xfff8))) {
      case JIT_REF_CODE:
      case JIT_REF_DATA:
       target->arg[1] = ((jit_value)jit->ip - (jit_value)jit->buf);
       break;
      case JIT_DATA_REF_CODE:
      case JIT_DATA_REF_DATA:
       target->arg[0] = ((jit_value)jit->ip - (jit_value)jit->buf);
       break;
      default: {
       jit_value pa = target->patch_addr;
       do { unsigned char* pos = (jit->buf + pa) + 1; int disp, size = 0; switch (*(unsigned char*)(jit->buf + pa)) { case 0xe8: case 0xe9: ++size; break; case 0x0f: if (!(*pos >= 0x70 && *pos <= 0x8f)) assert (0); ++size; ++pos; break; case 0xe0: case 0xe1: case 0xe2: case 0xeb: case 0x70: case 0x71: case 0x72: case 0x73: case 0x74: case 0x75: case 0x76: case 0x77: case 0x78: case 0x79: case 0x7a: case 0x7b: case 0x7c: case 0x7d: case 0x7e: case 0x7f: break; default: assert (0); } disp = (jit->ip) - pos; if (size) do { jit_internal_x86_imm_buf imb; imb.val = (int) (disp - 4); *(pos)++ = imb.b [0]; *(pos)++ = imb.b [1]; *(pos)++ = imb.b [2]; *(pos)++ = imb.b [3]; } while (0); else if ((((int)(disp - 1) >= -128 && (int)(disp - 1) <= 127))) do { *(pos) = (unsigned char)((disp - 1) & 0xff); ++(pos); } while (0); else assert (0); } while (0);
      }
     }
    } while (0);
    break;
  case JIT_JMP:
   op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
   if (op->code & 0x01) do { *(jit->ip)++ = (unsigned char)0xff; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|((((4))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
   else do { int t = ((!jit_is_label(jit, (void *)(a1)) ? (a1) : (((jit_value)jit->buf + ((jit_label *)(a1))->pos - (jit_value)jit->ip)))) - 5; do { *((jit->ip))++ = (unsigned char)0xe9; do { jit_internal_x86_imm_buf imb; imb.val = (int) ((t)); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0);
   break;
  case JIT_RET:
   if (!imm && (a1 != X86_EAX)) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_EAX)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
   if (imm) do { *(jit->ip)++ = (unsigned char)0xb8 + (X86_EAX); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a1)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
   jit_internal_emit_pop_callee_saved_regs(jit);
   if (jit_current_func_info(jit)->has_prolog) {
    do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((X86_ESP)))&0x07)<<3)|(((((X86_EBP)))&0x07))); } while (0); } while (0); } while (0);
    do { *(jit->ip)++ = (unsigned char)0x58 + (X86_EBP); } while (0);
   }
   do { *(jit->ip)++ = (unsigned char)0xc3; } while (0);
   break;
  case JIT_PUTARG: jit_internal_funcall_put_arg(jit, op); break;
  case JIT_FPUTARG: jit_internal_funcall_fput_arg(jit, op); break;
  case JIT_GETARG: jit_internal_emit_get_arg(jit, op); break;
  case JIT_MSG: jit_internal_emit_msg_op(jit, op); break;
  case JIT_TRACE: jit_internal_emit_trace_op(jit, op);
    while (((unsigned long) jit->ip) % 16)
     do { *(jit->ip)++ = (unsigned char)0x90; } while (0);
    break;
  case JIT_LD: jit_internal_emit_ld_op(jit, op, a1, a2); break;
  case JIT_LDX: jit_internal_emit_ldx_op(jit, op, a1, a2, a3); break;
  case JIT_FST: jit_internal_emit_sse_fst_op(jit, op, a1, a2); break;
  case JIT_FSTX: jit_internal_emit_sse_fstx_op(jit, op, a1, a2, a3); break;
  case JIT_FLD: jit_internal_emit_sse_fld_op(jit, op, a1, a2); break;
  case JIT_FLDX: jit_internal_emit_sse_fldx_op(jit, op, a1, a2, a3); break;
  case JIT_MEMCPY: jit_internal_emit_memcpy(jit, op, a1, a2, a3); break;
  case JIT_MEMSET: jit_internal_emit_memset(jit, op, a1, a2, a3, op->arg_size); break;
  case JIT_TRANSFER: jit_internal_emit_transfer_init(jit, op, a1, a2, a3, op->arg_size); break;
  case JIT_TRANSFER_CPY: jit_internal_emit_transfer_loop(jit, (jit_op *)a1); break;
  case JIT_TRANSFER_XOR: jit_internal_emit_transfer_op(jit, op, X86_XOR); break;
  case JIT_TRANSFER_AND: jit_internal_emit_transfer_op(jit, op, X86_AND); break;
  case JIT_TRANSFER_OR: jit_internal_emit_transfer_op(jit, op, X86_OR); break;
  case JIT_TRANSFER_ADD: jit_internal_emit_transfer_op(jit, op, X86_ADD); break;
  case JIT_TRANSFER_SUB: jit_internal_emit_transfer_op(jit, op, X86_SUB); break;
  case JIT_ALLOCA: break;
  case JIT_DECL_ARG: break;
  case JIT_RETVAL: break;
  case JIT_LABEL: ((jit_label *)a1)->pos = ((jit_value)jit->ip - (jit_value)jit->buf); break;
  case JIT_CODE_ALIGN:
    while (((unsigned long) jit->ip) % op->arg[0])
     do { *(jit->ip)++ = (unsigned char)0x90; } while (0);
    break;
  case JIT_REF_CODE:
  case JIT_REF_DATA:
   op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
   do { *(jit->ip)++ = (unsigned char)0xb8 + (a1); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((0xdeadbeefcafebabe)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
   break;
  case JIT_DATA_BYTE: break;
  case JIT_FULL_SPILL: break;
  default: found = 0;
 }
 if (found) return;
 switch (op->code) {
  case (JIT_MOV | 0x01): if (a1 != a2) do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0); break;
  case (JIT_MOV | 0x02):
   if (a2 == 0) do { *(jit->ip)++ = (((unsigned char)(X86_XOR)) << 3) + 3; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0);
   else do { *(jit->ip)++ = (unsigned char)0xb8 + (a1); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a2)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } while (0);
   break;
  case JIT_PREPARE: jit_internal_funcall_prepare(jit, op, a1 + a2);
      jit->push_count += jit_internal_emit_push_caller_saved_regs(jit, op);
      break;
  case JIT_PROLOG: jit_internal_emit_prolog_op(jit, op); break;
  case (JIT_ST | 0x02): do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0); break;
  case (JIT_ST | 0x01): do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_STX | 0x02): do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_STX | 0x01): do { switch ((op->arg_size)) { case 1: *(jit->ip)++ = (unsigned char)0x88; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x89; break; default: assert (0); } do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a3)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_FMOV | 0x01): do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x11; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a2)))&0x07)<<3)|(((((a1)))&0x07))); } while (0); } while (0); } while (0); break;
  case (JIT_FMOV | 0x02): do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x10; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((&op->flt_imm))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); } while (0); break;
  case (JIT_FADD | 0x01): jit_internal_emit_sse_alu_op(jit, op, X86_SSE_ADD); break;
  case (JIT_FSUB | 0x01): jit_internal_emit_sse_sub_op(jit, op, a1, a2, a3); break;
  case (JIT_FRSB | 0x01): jit_internal_emit_sse_sub_op(jit, op, a1, a3, a2); break;
  case (JIT_FMUL | 0x01): jit_internal_emit_sse_alu_op(jit, op, X86_SSE_MUL); break;
  case (JIT_FDIV | 0x01): jit_internal_emit_sse_div_op(jit, a1, a2, a3); break;
                case (JIT_FNEG | 0x01): jit_internal_emit_sse_neg_op(jit, op, a1, a2); break;
  case (JIT_FBLT | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a2, a3, jit_internal_X86_CC_LT); break;
                case (JIT_FBGT | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a2, a3, jit_internal_X86_CC_GT); break;
                case (JIT_FBGE | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a2, a3, jit_internal_X86_CC_GE); break;
                case (JIT_FBLE | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a3, a2, jit_internal_X86_CC_GE); break;
                case (JIT_FBEQ | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a3, a2, jit_internal_X86_CC_EQ); break;
                case (JIT_FBNE | 0x01): jit_internal_emit_sse_branch(jit, op, a1, a3, a2, jit_internal_X86_CC_NE); break;
  case (JIT_EXT | 0x01): do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x2a; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0); break;
                case (JIT_TRUNC | 0x01): do { *(jit->ip)++ = (unsigned char)0xf2; *(jit->ip)++ = (unsigned char)0x0f; *(jit->ip)++ = (unsigned char)0x2c; do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0); break;
  case (JIT_CEIL | 0x01): jit_internal_emit_sse_floor(jit, a1, a2, 0); break;
                case (JIT_FLOOR | 0x01): jit_internal_emit_sse_floor(jit, a1, a2, 1); break;
  case (JIT_ROUND | 0x01): jit_internal_emit_sse_round(jit, op, a1, a2); break;
  case (JIT_FRET | 0x01): jit_internal_emit_fret_op(jit, op); break;
  case JIT_FRETVAL: jit_internal_emit_fretval_op(jit, op); break;
  case (JIT_UREG): jit_internal_emit_ureg(jit, a1, a2); break;
  case (JIT_LREG): jit_internal_emit_lreg(jit, a1, a2); break;
  case (JIT_SYNCREG): jit_internal_emit_ureg(jit, a1, a2); break;
  case JIT_RENAMEREG: do { switch (((sizeof(void *)))) { case 1: *(jit->ip)++ = (unsigned char)0x8a; break; case 2: *(jit->ip)++ = (unsigned char)0x66; case 4: *(jit->ip)++ = (unsigned char)0x8b; break; default: assert (0); } do { do { *(((jit->ip)))++ = ((((3)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((((a2)))&0x07))); } while (0); } while (0); } while (0); break;
  case JIT_CODESTART: break;
  case JIT_NOP: break;
  case (JIT_X86_STI | 0x02): do { if ((op->arg_size) == 1) { *(jit->ip)++ = (unsigned char)0xc6; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); do { *((jit->ip)) = (unsigned char)(((a2)) & 0xff); ++((jit->ip)); } while (0); } else if ((op->arg_size) == 2) { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0xc7; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); do { *(short*)((jit->ip)) = ((a2)); ((jit->ip)) += 2; } while (0); } else { *(jit->ip)++ = (unsigned char)0xc7; do { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a2)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
  case (JIT_X86_STI | 0x01): do { if ((op->arg_size) == 1) { *(jit->ip)++ = (unsigned char)0xc6; do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *((jit->ip)) = (unsigned char)(((a2)) & 0xff); ++((jit->ip)); } while (0); } else if ((op->arg_size) == 2) { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *(short*)((jit->ip)) = ((a2)); ((jit->ip)) += 2; } while (0); } else { *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == X86_ESP) { if (((0)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); break; } if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a1)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a2)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
  case (JIT_X86_STXI | 0x02): do { if ((op->arg_size) == 1) { *(jit->ip)++ = (unsigned char)0xc6; do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *((jit->ip)) = (unsigned char)(((a3)) & 0xff); ++((jit->ip)); } while (0); } else if ((op->arg_size) == 2) { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0xc7; do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *(short*)((jit->ip)) = ((a3)); ((jit->ip)) += 2; } while (0); } else { *(jit->ip)++ = (unsigned char)0xc7; do { if (((a2)) == X86_ESP) { if (((a1)) == 0) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); } else if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((X86_ESP)&0x07)<<3)|(((X86_ESP)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } break; } if (((a1)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); break; } if ((((int)(((a1))) >= -128 && (int)(((a1))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a1))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((((a2)))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a1))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a3)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
  case (JIT_X86_STXI | 0x01): do { if ((op->arg_size) == 1) { *(jit->ip)++ = (unsigned char)0xc6; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *((jit->ip)) = (unsigned char)(((a3)) & 0xff); ++((jit->ip)); } while (0); } else if ((op->arg_size) == 2) { *(jit->ip)++ = (unsigned char)0x66; *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { *(short*)((jit->ip)) = ((a3)); ((jit->ip)) += 2; } while (0); } else { *(jit->ip)++ = (unsigned char)0xc7; do { if (((a1)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a1)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|((((0))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|((((((a1))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) ((a3)); *((jit->ip))++ = imb.b [0]; *((jit->ip))++ = imb.b [1]; *((jit->ip))++ = imb.b [2]; *((jit->ip))++ = imb.b [3]; } while (0); } } while (0); break;
  case (JIT_X86_ADDMUL | 0x01): do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((0)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((0))) >= -128 && (int)(((0))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((0))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((0))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_X86_ADDMUL | 0x02): do { *(jit->ip)++ = (unsigned char)0x8d; do { if ((((-1))) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a2)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((a3)) == 0 && (((-1))) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); } else if ((((int)(((a3))) >= -128 && (int)(((a3))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((a3))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((op->arg_size)))&0x03)<<6)|(((((a2))&0x7)&0x07)<<3)|(((((((-1)))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((a3))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  case (JIT_X86_ADDIMM): {
   jit_value tmp;
   memcpy(&tmp, &op->flt_imm, sizeof(jit_value));
   do { *(jit->ip)++ = (unsigned char)0x8d; do { if (((a2)) == (-1)) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3)))&0x07)<<3)|(((5)&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((tmp))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } else if (((tmp)) == 0 && ((a2)) != X86_EBP) { do { *(((jit->ip)))++ = ((((0)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); } else if ((((int)(((tmp))) >= -128 && (int)(((tmp))) <= 127))) { do { *(((jit->ip)))++ = ((((1)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { *(((jit->ip))) = (unsigned char)((((tmp))) & 0xff); ++(((jit->ip))); } while (0); } else { do { *(((jit->ip)))++ = ((((2)&0x03)<<6)|(((((a1)))&0x07)<<3)|(((4)&0x07))); } while (0); do { *(((jit->ip)))++ = ((((((0)))&0x03)<<6)|(((((a3))&0x7)&0x07)<<3)|((((((a2))&0x7))&0x07))); } while (0); do { jit_internal_x86_imm_buf imb; imb.val = (int) (((tmp))); *(((jit->ip)))++ = imb.b [0]; *(((jit->ip)))++ = imb.b [1]; *(((jit->ip)))++ = imb.b [2]; *(((jit->ip)))++ = imb.b [3]; } while (0); } } while (0); } while (0); break;
  }
  default: printf("common86: unknown operation (opcode: 0x%x)\n", ((jit_opcode) (op->code & 0xfff8)) >> 3);
 }
}
static jit_hw_reg * jit_internal_rmap_is_associated(jit_rmap * rmap, int reg_id, int fp, jit_value * virt_reg);
static inline int jit_internal_bufprint(char *buf, const char *format, ...) {
 va_list ap;
 va_start(ap, format);
 int result = vsprintf(buf + strlen(buf), format, ap);
 va_end(ap);
 return result;
}
static void jit_internal_compiler_based_debugger(struct jit * jit)
{
 char obj_file_name[] = "myjitXXXXXX";
 int obj_file_fd = mkstemp(obj_file_name);
 char * cmd1_fmt = "gcc -x assembler -c -o %s -";
 char * cmd2_fmt = "objdump -d -M intel %s";
 char cmd1[strlen(cmd1_fmt) + strlen(obj_file_name) + 1];
 char cmd2[strlen(cmd2_fmt) + strlen(obj_file_name) + 1];
 sprintf(cmd1, cmd1_fmt, obj_file_name);
 FILE * f = popen(cmd1, "w");
 int size = jit->ip - jit->buf;
 fprintf (f, ".text\n.align 4\n.globl main\n.type main,@function\nmain:\n");
 for (int i = 0; i < size; i++)
  fprintf(f, ".byte %d\n", (unsigned int) jit->buf[i]);
 pclose(f);
 sprintf(cmd2, cmd2_fmt, obj_file_name);
 system(cmd2);
 close(obj_file_fd);
 unlink(obj_file_name);
}
typedef struct jit_disasm {
 char *indent_template;
 char *reg_template;
 char *freg_template;
 char *arg_template;
 char *farg_template;
 char *reg_fp_template;
 char *reg_out_template;
 char *reg_imm_template;
 char *reg_fimm_template;
 char *reg_unknown_template;
 char *label_template;
 char *label_forward_template;
 char *generic_addr_template;
 char *generic_value_template;
} jit_disasm;
struct jit_disasm jit_disasm_general = {
 .indent_template = "    ",
 .reg_template = "r%i",
 .freg_template = "fr%i",
 .arg_template = "arg%i",
 .farg_template = "farg%i",
 .reg_out_template = "out",
 .reg_fp_template = "fp",
 .reg_imm_template = "imm",
 .reg_fimm_template = "fimm",
 .reg_unknown_template = "(unknown reg.)",
 .label_template = "L%i",
 .label_forward_template = "L%i",
 .generic_addr_template = "<addr: 0x%lx>",
 .generic_value_template = "0x%lx",
};
struct jit_disasm jit_disasm_compilable = {
 .indent_template = "    ",
 .reg_template = "R(%i)",
 .freg_template = "FR(%i)",
 .arg_template = "arg(%i)",
 .farg_template = "farg(%i)",
 .reg_fp_template = "R_FP",
 .reg_out_template = "R_OUT",
 .reg_imm_template = "R_IMM",
 .reg_fimm_template = "FR_IMM",
 .reg_unknown_template = "(unknown reg.)",
 .label_template = "label_%03i",
 .label_forward_template = "/* label_%03i */ JIT_FORWARD",
 .generic_addr_template = "<addr: 0x%lx>",
 .generic_value_template = "%li",
};
char * jit_get_op_name(struct jit_op * op)
{
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_MOV: return "mov";
  case JIT_LD: return "ld";
  case JIT_LDX: return "ldx";
  case JIT_ST: return "st";
  case JIT_STX: return "stx";
  case JIT_MEMCPY:return "memcpy";
  case JIT_MEMSET:return "memset";
  case JIT_JMP: return "jmp";
  case JIT_PATCH: return ".patch";
  case JIT_PREPARE: return "prepare";
  case JIT_PUTARG: return "putarg";
  case JIT_CALL: return "call";
  case JIT_RET: return "ret";
  case JIT_PROLOG: return "prolog";
  case JIT_GETARG: return "getarg";
  case JIT_RETVAL: return "retval";
  case JIT_ALLOCA: return "alloca";
  case JIT_DECL_ARG: return "declare_arg";
  case JIT_ADD: return "add";
  case JIT_ADDC: return "addc";
  case JIT_ADDX: return "addx";
  case JIT_SUB: return "sub";
  case JIT_SUBC: return "subc";
  case JIT_SUBX: return "subx";
  case JIT_RSB: return "rsb";
  case JIT_NEG: return "neg";
  case JIT_MUL: return "mul";
  case JIT_HMUL: return "hmul";
  case JIT_DIV: return "div";
  case JIT_MOD: return "mod";
  case JIT_OR: return "or";
  case JIT_XOR: return "xor";
  case JIT_AND: return "and";
  case JIT_LSH: return "lsh";
  case JIT_RSH: return "rsh";
  case JIT_NOT: return "not";
  case JIT_LT: return "lt";
  case JIT_LE: return "le";
  case JIT_GT: return "gt";
  case JIT_GE: return "ge";
  case JIT_EQ: return "eq";
  case JIT_NE: return "ne";
  case JIT_BLT: return "blt";
  case JIT_BLE: return "ble";
  case JIT_BGT: return "bgt";
  case JIT_BGE: return "bge";
  case JIT_BEQ: return "beq";
  case JIT_BNE: return "bne";
  case JIT_BMS: return "bms";
  case JIT_BMC: return "bmc";
  case JIT_BOADD: return "boadd";
  case JIT_BOSUB: return "bosub";
  case JIT_BNOADD:return "bnoadd";
  case JIT_BNOSUB:return "bnosub";
  case JIT_UREG: return ".ureg";
  case JIT_LREG: return ".lreg";
  case JIT_CODESTART: return ".code";
  case JIT_LABEL: return ".label";
  case JIT_SYNCREG: return ".syncreg";
  case JIT_RENAMEREG: return ".renamereg";
  case JIT_MSG: return "msg";
  case JIT_COMMENT: return ".comment";
  case JIT_NOP: return "nop";
  case JIT_CODE_ALIGN: return ".align";
  case JIT_DATA_BYTE: return ".byte";
  case JIT_DATA_BYTES: return ".bytes";
  case JIT_DATA_REF_CODE: return ".ref_code";
  case JIT_DATA_REF_DATA: return ".ref_data";
  case JIT_REF_CODE: return "ref_code";
  case JIT_REF_DATA: return "ref_data";
  case JIT_FULL_SPILL: return ".full_spill";
  case JIT_TRACE: return ".trace";
  case JIT_FORCE_SPILL: return "jit_internal_force_spill";
  case JIT_FORCE_ASSOC: return "jit_internal_force_assoc";
  case JIT_MARK: return "mark";
  case JIT_TOUCH: return "touch";
  case JIT_TRANSFER: return "transfer";
  case JIT_TRANSFER_CPY: return "transfer_cpy";
  case JIT_TRANSFER_AND: return "transfer_and";
  case JIT_TRANSFER_OR: return "transfer_or";
  case JIT_TRANSFER_XOR: return "transfer_xor";
  case JIT_TRANSFER_ADD: return "transfer_add";
  case JIT_TRANSFER_SUB: return "transfer_sub";
  case JIT_FMOV: return "fmov";
  case JIT_FADD: return "fadd";
  case JIT_FSUB: return "fsub";
  case JIT_FRSB: return "frsb";
  case JIT_FMUL: return "fmul";
  case JIT_FDIV: return "fdiv";
  case JIT_FNEG: return "fneg";
  case JIT_FRETVAL: return "fretval";
  case JIT_FPUTARG: return "fputarg";
  case JIT_EXT: return "ext";
  case JIT_ROUND: return "round";
  case JIT_TRUNC: return "trunc";
  case JIT_FLOOR: return "floor";
  case JIT_CEIL: return "ceil";
  case JIT_FBLT: return "fblt";
  case JIT_FBLE: return "fble";
  case JIT_FBGT: return "fbgt";
  case JIT_FBGE: return "fbge";
  case JIT_FBEQ: return "fbeq";
  case JIT_FBNE: return "fbne";
  case JIT_FLD: return "fld";
  case JIT_FLDX: return "fldx";
  case JIT_FST: return "fst";
  case JIT_FSTX: return "fstx";
  case JIT_FRET: return "fret";
  default: return "(unknown)";
 }
}
void jit_get_reg_name(struct jit_disasm *disasm, char * r, int reg)
{
 if (reg == (((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((0) & 0xfffffff) << 4))) strcpy(r, disasm->reg_fp_template);
 else if (reg == (((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((1) & 0xfffffff) << 4))) strcpy(r, disasm->reg_out_template);
 else if (reg == (((((0)) & 0x01) | ((((1)) & 0x03) << 1) | ((0) & 0xfffffff) << 4))) strcpy(r, disasm->reg_imm_template);
 else if (reg == (((((1)) & 0x01) | ((((1)) & 0x03) << 1) | ((0) & 0xfffffff) << 4))) strcpy(r, disasm->reg_fimm_template);
 else {
  if ((((reg) >> 1) & 0x03) == (0)) {
   if (((reg) & 0x01) == (0)) sprintf(r, disasm->reg_template, (((reg) >> 4) & 0xfffffff));
   else sprintf(r, disasm->freg_template, (((reg) >> 4) & 0xfffffff));
  }
  else if ((((reg) >> 1) & 0x03) == (3)) {
   if (((reg) & 0x01) == (0)) sprintf(r, disasm->arg_template, (((reg) >> 4) & 0xfffffff));
   else sprintf(r, disasm->farg_template, (((reg) >> 4) & 0xfffffff));
  } else sprintf(r, "%s", disasm->reg_unknown_template);
 }
}
static void jit_internal_print_rmap_callback(jit_tree_key key, jit_tree_value value, void *disasm)
{
 char buf[256];
 jit_get_reg_name((struct jit_disasm *)disasm, buf, key);
 printf("%s=%s ", buf, ((jit_hw_reg *)value)->name);
}
static void jit_internal_print_reg_liveness_callback(jit_tree_key key, jit_tree_value value, void *disasm)
{
 char buf[256];
 jit_get_reg_name(disasm, buf, key);
 printf("%s ", buf);
}
static inline int jit_op_is_cflow(jit_op * op)
{
 if (((((jit_opcode) (op->code & 0xfff8)) == JIT_CALL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_JMP)) && ((op->code & 0x02))) return 1;
 if (jit_internal_is_cond_branch_op(op)) return 1;
 return 0;
}
static jit_tree * jit_internal_prepare_labels(struct jit * jit)
{
 long x = 1;
 jit_tree * n = NULL;
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH) {
   n = jit_tree_insert(n, (long) op, (void *)x, NULL);
   n = jit_tree_insert(n, op->arg[0], (void *) -x, NULL);
   x++;
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) {
   n = jit_tree_insert(n, op->arg[0], (void *)x, NULL);
   x++;
  }
 }
 return n;
}
static inline void jit_internal_print_addr(struct jit_disasm *disasm, char *buf, jit_tree *labels, jit_op *op, int arg_pos)
{
 void *arg = (void *)op->arg[arg_pos];
 jit_tree *label_item = jit_tree_search(labels, (long) op);
 if (label_item) jit_internal_bufprint(buf, disasm->label_forward_template, - (long) label_item->value);
 else {
  label_item = jit_tree_search(labels, (long) arg);
  if (label_item) jit_internal_bufprint(buf, disasm->label_template, (long) label_item->value);
  else jit_internal_bufprint(buf, disasm->generic_addr_template, arg);
 }
}
static inline void jit_internal_print_arg(struct jit_disasm *disasm, char * buf, struct jit_op * op, int arg)
{
 long a = op->arg[arg - 1];
 if ((((op)->spec >> ((arg) - 1) * 2) & 0x03) == 0x02) jit_internal_bufprint(buf, disasm->generic_value_template, a);
 if (((((op)->spec >> ((arg) - 1) * 2) & 0x03) == 0x01) || ((((op)->spec >> ((arg) - 1) * 2) & 0x03) == 0x03)) {
  char value[256];
  jit_get_reg_name(disasm, value, a);
  strcat(buf, value);
 }
}
static inline void jit_internal_print_str(char * buf, char * str)
{
 strcat(buf, " \"");
 for (int i = 0; i < strlen(str); i++) {
  if (str[i] >= 32) {
   int s = strlen(buf);
   buf[s++] = str[i];
   buf[s] = '\0';
  } else {
   char xbuf[16];
   switch (str[i]) {
    case 9: strcpy(xbuf, "\\t"); break;
    case 10: strcpy(xbuf, "\\n"); break;
    case 13: strcpy(xbuf, "\\r"); break;
    default: sprintf(xbuf, "\\x%02x", str[i]);
   }
   strcat(buf, xbuf);
  }
 }
 strcat(buf, "\"");
}
static void jit_internal_print_args(struct jit_disasm *disasm, char *linebuf, jit_op *op, jit_tree *labels)
{
 for (int i = 1; i <= 3; i++) {
  if ((((op)->spec >> ((i) - 1) * 2) & 0x03) == 0x00) continue;
  strcat(linebuf, i == 1 ? " " : ", ");
  if ((i == 1) && jit_op_is_cflow(op)) jit_internal_print_addr(disasm, linebuf, labels, op, 0);
  else jit_internal_print_arg(disasm, linebuf, op, i);
 }
}
void jit_internal_print_full_op_name(char *linebuf, jit_op *op)
{
 char *op_name = jit_get_op_name(op);
 strcat(linebuf, op_name);
 if ((((jit_opcode) (op->code & 0xfff8)) == JIT_CALL) && ((op->code & 0x0007) & 0x02)) return;
 if ((op->code & 0x0007) & 0x02) strcat(linebuf, "i");
 if ((op->code & 0x0007) & 0x01) strcat(linebuf, "r");
 if ((op->code & 0x0007) & 0x04) strcat(linebuf, "_u");
}
static int jit_internal_print_load_op(struct jit_disasm *disasm, char *linebuf, jit_op *op)
{
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_LREG:
   strcat(linebuf, disasm->indent_template);
   strcat(linebuf, jit_get_op_name(op));
   while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
   jit_get_reg_name(disasm, linebuf + strlen(linebuf), op->arg[1]);
   return 1;
  case JIT_UREG:
  case JIT_SYNCREG:
   strcat(linebuf, disasm->indent_template);
   strcat(linebuf, jit_get_op_name(op));
   while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
   jit_get_reg_name(disasm, linebuf + strlen(linebuf), op->arg[0]);
   return 1;
  case JIT_RENAMEREG: {
    jit_value reg;
    jit_internal_rmap_is_associated(op->prev->regmap, op->arg[1], 0, &reg);
    strcat(linebuf, disasm->indent_template);
    strcat(linebuf, jit_get_op_name(op));
    strcat(linebuf, " ");
    while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
    jit_get_reg_name(disasm, linebuf + strlen(linebuf), reg);
    return 1;
   }
  case JIT_FULL_SPILL:
   strcat(linebuf, disasm->indent_template);
   strcat(linebuf, jit_get_op_name(op));
   return 1;
  default:
   return 0;
 }
}
void jit_internal_print_comment(char *linebuf, jit_op *op)
{
 char *str = (char *)op->arg[0];
 jit_internal_bufprint(linebuf, "// ");
 for (int i = 0; i < strlen(str); i++) {
  if ((str[i] == '\r') || (str[i] == '\n')) jit_internal_bufprint(linebuf, "\n// ");
  else jit_internal_bufprint(linebuf, "%c", str[i]);
 }
}
int jit_internal_print_op(FILE *f, struct jit_disasm * disasm, struct jit_op *op, jit_tree *labels, int verbosity)
{
 char linebuf[(8192)];
 linebuf[0] = '\0';
 if ((((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH)) {
  jit_tree * lab = jit_tree_search(labels, (long)op->arg[0]);
  if (lab) {
   jit_internal_bufprint(linebuf, disasm->label_template, (((long)lab->value) < 0 ? - ((long)lab->value) : (long)lab->value));
   jit_internal_bufprint(linebuf, ":");
  }
  goto print;
 }
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_COMMENT) {
  jit_internal_print_comment(linebuf, op);
  goto print;
 }
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_TRACE) {
  strcat(linebuf, disasm->indent_template);
  strcat(linebuf, ".trace");
  goto print;
 }
 char * op_name = jit_get_op_name(op);
 if ((op_name[0] == '.') && (verbosity & (0x100))) {
  if (jit_internal_print_load_op(disasm, linebuf, op)) goto print;
 }
 strcat(linebuf, disasm->indent_template);
 if (op_name[0] == '.') {
  switch (((jit_opcode) (op->code & 0xfff8))) {
   case JIT_DATA_BYTE:
   case JIT_CODE_ALIGN:
    jit_internal_bufprint(linebuf, "%s ", op_name);
    while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
    jit_internal_bufprint(linebuf, disasm->generic_value_template, op->arg[0]);
    goto print;
   case JIT_DATA_BYTES:
    jit_internal_bufprint(linebuf, "%s ", op_name);
    while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
    for (int i = 0; i < op->arg[0]; i++) {
     jit_internal_bufprint(linebuf, disasm->generic_value_template, ((unsigned char *)op->addendum)[i]);
     jit_internal_bufprint(linebuf, " ");
    }
    goto print;
   case JIT_DATA_REF_CODE:
   case JIT_DATA_REF_DATA:
    jit_internal_bufprint(linebuf, "%s ", op_name);
    while (strlen((linebuf)) < (13)) { strcat((linebuf), " "); };
    jit_internal_print_addr(disasm, linebuf, labels, op, 0);
    goto print;
   default:
    goto print;
  }
 }
 jit_internal_print_full_op_name(linebuf, op);
 while (strlen((linebuf)) < (12)) { strcat((linebuf), " "); };
 if (op->arg_size == 1) strcat(linebuf, " (byte)");
 if (op->arg_size == 2) strcat(linebuf, " (word)");
 if (op->arg_size == 4) strcat(linebuf, " (dword)");
 if (op->arg_size == 8) strcat(linebuf, " (qword)");
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_PREPARE: break;
  case JIT_MSG:
   jit_internal_print_str(linebuf, (char *)op->arg[0]);
   if (!(op->code & 0x02)) strcat(linebuf, ", "), jit_internal_print_arg(disasm, linebuf, op, 2);
   break;
  case JIT_REF_CODE:
  case JIT_REF_DATA:
   strcat(linebuf, " ");
   jit_internal_print_arg(disasm, linebuf, op, 1);
   strcat(linebuf, ", ");
   jit_internal_print_addr(disasm, linebuf, labels, op, 1);
   break;
  case JIT_DECL_ARG:
   switch (op->arg[0]) {
    case JIT_SIGNED_NUM: strcat(linebuf, " integer"); break;
    case JIT_UNSIGNED_NUM: strcat(linebuf, " uns. integer"); break;
    case JIT_FLOAT_NUM: strcat(linebuf, " float"); break;
    case JIT_PTR: strcat(linebuf, " ptr"); break;
    default: assert(0);
   };
   strcat(linebuf, ", ");
   jit_internal_print_arg(disasm, linebuf, op, 2);
   break;
  default:
   jit_internal_print_args(disasm, linebuf, op, labels);
 }
print:
 fprintf(f, "%s", linebuf);
 return strlen(linebuf);
}
int jit_internal_print_op_compilable(struct jit_disasm *disasm, struct jit_op * op, jit_tree * labels)
{
 char linebuf[(8192)];
 linebuf[0] = '\0';
 jit_tree * lab = jit_tree_search(labels, (long)op);
 if (lab && ((long) lab->value > 0)) {
  jit_internal_bufprint(linebuf, "// ");
  jit_internal_bufprint(linebuf, disasm->label_template, (long)lab->value);
  jit_internal_bufprint(linebuf, ":\n");
 }
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_COMMENT) {
  jit_internal_print_comment(linebuf, op);
  goto direct_print;
 }
 strcat(linebuf, disasm->indent_template);
 if ((jit_op_is_cflow(op) && ((void *)op->arg[0] == (NULL)))
 || (((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_REF_DATA)
 || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_DATA))
  jit_internal_bufprint(linebuf, "jit_op * op_%li = ", (((unsigned long) (op)) >> 4));
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_LABEL: {
   jit_internal_bufprint(linebuf, "jit_label * ");
   jit_tree * lab = jit_tree_search(labels, (long)op->arg[0]);
   if (lab) jit_internal_bufprint(linebuf, disasm->label_template, (long) lab->value);
   jit_internal_bufprint(linebuf, " = jit_get_label(p");
   goto print;
  }
  case JIT_PATCH:
   jit_internal_bufprint(linebuf, "jit_patch  (p, op_%li", (((unsigned long) (op->arg[0])) >> 4));
   goto print;
  case JIT_DATA_BYTE:
   jit_internal_bufprint(linebuf, "jit_data_byte(p, ");
   jit_internal_bufprint(linebuf, disasm->generic_value_template, op->arg[0]);
   goto print;
  case JIT_DATA_BYTES:
   for (int i = 0; i < op->arg[0]; i++) {
    jit_internal_bufprint(linebuf, "jit_data_byte(p, ");
    jit_internal_bufprint(linebuf, disasm->generic_value_template, ((unsigned char *)op->addendum) [i]);
    if (i < op->arg[0] - 1) jit_internal_bufprint(linebuf, ");\n");
   }
   goto print;
  case JIT_REF_CODE:
  case JIT_REF_DATA:
   jit_internal_bufprint(linebuf, "jit_%s(p, ", jit_get_op_name(op));
   jit_internal_print_arg(disasm, linebuf, op, 1);
   strcat(linebuf, ", ");
   jit_internal_print_addr(disasm, linebuf, labels, op, 1);
   goto print;
  case JIT_DATA_REF_CODE:
  case JIT_DATA_REF_DATA:
   jit_internal_bufprint(linebuf, "jit_data_%s(p, ", jit_get_op_name(op) + 1);
   jit_internal_print_addr(disasm, linebuf, labels, op, 0);
   goto print;
  case JIT_CODE_ALIGN:
   jit_internal_bufprint(linebuf, "jit_code_align  (p, ");
   jit_internal_bufprint(linebuf, disasm->generic_value_template, op->arg[0]);
   goto print;
  case JIT_PREPARE:
   jit_internal_bufprint(linebuf, "jit_prepare(p");
   goto print;
  default:
   break;
 }
 if (jit_get_op_name(op)[0] == '.') goto direct_print;
 strcat(linebuf, "jit_");
 jit_internal_print_full_op_name(linebuf, op);
 while (strlen((linebuf)) < (15)) { strcat((linebuf), " "); };
 strcat(linebuf, "(p,");
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_MSG:
   jit_internal_print_str(linebuf, (char *)op->arg[0]);
   if (!(op->code & 0x02)) strcat(linebuf, ", "), jit_internal_print_arg(disasm, linebuf, op, 2);
   break;
  case JIT_DECL_ARG:
   switch (op->arg[0]) {
    case JIT_SIGNED_NUM: strcat(linebuf, "JIT_SIGNED_NUM"); break;
    case JIT_UNSIGNED_NUM: strcat(linebuf, "JIT_UNSIGNED_NUM"); break;
    case JIT_FLOAT_NUM: strcat(linebuf, "JIT_FLOAT_NUM"); break;
    case JIT_PTR: strcat(linebuf, "JIT_PTR"); break;
    default: assert(0);
   };
   strcat(linebuf, ", ");
   jit_internal_print_arg(disasm, linebuf, op, 2);
   break;
  default:
   jit_internal_print_args(disasm, linebuf, op, labels);
 }
 if (op->arg_size) jit_internal_bufprint(linebuf, ", %i", op->arg_size);
print:
 strcat(linebuf, ");");
direct_print:
 printf("%s", linebuf);
 return strlen(linebuf);
}
static void jit_dump_ops_compilable(struct jit *jit, jit_tree *labels)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  jit_internal_print_op_compilable(&jit_disasm_compilable, op, labels);
  printf("\n");
 }
}
static void jit_dump_ops_general(struct jit *jit, jit_tree *labels, int verbosity)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  int size = jit_internal_print_op(stdout, &jit_disasm_general, op, labels, verbosity);
  if (size == 0) return;
  for (; size < 35; size++)
   printf(" ");
  if ((verbosity & (0x400)) && (op->live_in) && (op->live_out)) {
   printf("In: ");
   jit_tree_walk(op->live_in->root, jit_internal_print_reg_liveness_callback, &jit_disasm_general);
   printf("\tOut: ");
   jit_tree_walk(op->live_out->root, jit_internal_print_reg_liveness_callback, &jit_disasm_general);
  }
  if ((verbosity & (0x200)) && (op->regmap)) {
   printf("\tAssoc: ");
   jit_tree_walk(op->regmap->map, jit_internal_print_rmap_callback, &jit_disasm_general);
  }
  printf("\n");
 }
}
static char *jit_internal_platform_id()
{
 return "i386";
}
static inline void jit_internal_print_op_bytes(FILE *f, struct jit *jit, jit_op *op) {
 for (int i = 0; i < op->code_length; i++)
  fprintf(f, " %02x", jit->buf[op->code_offset + i]);
 fprintf(f, "\n.nl\n");
}
static FILE *jit_internal_open_disasm()
{
 int fds[2];
 pipe(fds);
 pid_t child = fork();
 if (child == 0) {
  close(fds[1]);
  dup2(fds[0], STDIN_FILENO);
  char *path;
  path = "./myjit-disasm";
  execlp(path, path, NULL);
  path = "myjit-disasm";
  execlp(path, path, NULL);
  path = getenv("MYJIT_DISASM");
  if (path) execlp(path, path, NULL);
  printf("myjit-disasm not found\n\n");
  printf("In order to list myjit operations along with the machine code, the MyJIT disassembler has to be present in the current directory or its path has to be specified in the MYJIT_DISASM environment variable.\nThe disassembler's source code can be found in the \"disasm/\" directory.\n\n");
  exit(1);
 }
 close(fds[0]);
 FILE * f = fdopen(fds[1], "w");
 return f;
}
static jit_op *jit_internal_print_combined_op(FILE *f, struct jit *jit, struct jit_op *op, jit_tree *labels)
{
 jit_opcode opcode = ((jit_opcode) (op->code & 0xfff8));
 if ((opcode == JIT_DATA_BYTE) || (opcode == JIT_DATA_BYTES)) {
  fprintf(f, ".text\n%s.byte\n", jit_disasm_general.indent_template);
  fprintf(f, ".data\n");
  while (op && ((((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTES))) {
   if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTE) fprintf(f, "%02x ", (unsigned char) op->arg[0]);
   if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTES) {
    for (int i = 0; i < op->arg[0]; i++)
     fprintf(f, "%02x ", ((unsigned char *) op->addendum)[i]);
   }
   op = op->next;
  }
  fprintf(f, "\n");
  if (!op) return NULL;
  op = op->prev;
  return op;
 }
 if (opcode == JIT_COMMENT) {
  fprintf(f, ".comment\n");
  jit_internal_print_op(f, &jit_disasm_general, op, labels, (0x100));
  fprintf(f, "\n");
  return op;
 }
 fprintf(f, ".text\n");
 jit_internal_print_op(f, &jit_disasm_general, op, labels, (0x100));
 fprintf(f, "\n");
 switch (opcode) {
  case JIT_CODE_ALIGN:
   if (op->next) {
    fprintf(f, "\n.nl\n");
    fprintf(f, ".addr=%lx\n", (unsigned long) (jit->buf + op->next->code_offset));
   }
   break;
  case JIT_DATA_REF_CODE:
  case JIT_DATA_REF_DATA:
   fprintf(f, ".data\n");
   jit_internal_print_op_bytes(f, jit, op);
   break;
  default:
   if (!op->code_length) break;
   fprintf(f, ".%s\n", jit_internal_platform_id());
   jit_internal_print_op_bytes(f, jit, op);
 }
 return op;
}
static void jit_dump_ops_combined(struct jit *jit, jit_tree *labels)
{
 FILE *f = jit_internal_open_disasm();
 fprintf(f, ".addr=%lx\n", (unsigned long)jit->buf);
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  op = jit_internal_print_combined_op(f, jit, op, labels);
  if (!op) break;
 }
 fclose(f);
 wait(NULL);
}
void jit_dump_ops(struct jit * jit, int verbosity)
{
 if (!(verbosity & ((0x02) | (0x08) | (0x04))))
  verbosity |= (0x01);
 jit_tree * labels = jit_internal_prepare_labels(jit);
 if (verbosity & (0x01)) jit_dump_ops_general(jit, labels, verbosity);
 if (verbosity & (0x02)) jit_internal_compiler_based_debugger(jit);
 if (verbosity & (0x08)) jit_dump_ops_compilable(jit, labels);
 if (verbosity & (0x04)) jit_dump_ops_combined(jit, labels);
 jit_tree_free(labels);
}
void jit_trace_op(struct jit *jit, jit_op *op, int verbosity)
{
 jit_tree * labels = jit_internal_prepare_labels(jit);
 if (verbosity & (0x01)) {
  jit_internal_print_op(stdout, &jit_disasm_general, op, labels, verbosity);
  printf("\n");
 }
 if (verbosity & (0x04)) {
  FILE *f = jit_internal_open_disasm();
  fprintf(f, "..addr=%lx\n", (unsigned long) op->code_offset);
  jit_internal_print_combined_op(f, jit, op, labels);
  fclose(f);
  wait(NULL);
 }
 jit_tree_free(labels);
}
void jit_trace_callback(struct jit *jit, jit_op *op, int verbosity, int trace)
{
 if (trace & (1)) jit_trace_op(jit, op->prev, verbosity);
 if (trace & (2)) jit_trace_op(jit, op->next, verbosity);
}
static void jit_dead_code_analysis(struct jit *jit, int remove_dead_code);
static inline void jit_expand_patches_and_labels(struct jit *jit);
static inline void jit_flw_analysis(struct jit *jit);
static inline void jit_prepare_reg_counts(struct jit *jit);
static inline void jit_prepare_arguments(struct jit *jit);
void jit_get_reg_name(struct jit_disasm *disasm, char * r, int reg);
static struct jit_disasm jit_debugging_disasm = {
 .indent_template = "    ",
 .reg_template = "r%i",
 .freg_template = "fr%i",
 .arg_template = "arg%i",
 .farg_template = "farg%i",
 .reg_out_template = "out",
 .reg_fp_template = "fp",
 .reg_imm_template = "imm",
 .reg_fimm_template = "fimm",
 .reg_unknown_template = "(unknown reg.)",
 .label_template = "<label>",
 .label_forward_template = "<label>",
 .generic_addr_template = "<addr: 0x%lx>",
 .generic_value_template = "0x%lx",
};
static void jit_internal_report_warning(struct jit *jit, jit_op *op, char *desc)
{
 fprintf(stdout, "%s at function `%s' (%s:%i)\n", desc, op->debug_info->function, op->debug_info->filename, op->debug_info->lineno);
 jit_internal_print_op(stdout, &jit_debugging_disasm, op, NULL, 0);
 fprintf(stdout, "\n");
}
static void jit_internal_append_msg(char *buf, char *format, ...)
{
 va_list ap;
 if (strlen(buf)) strcat(buf, ", ");
 va_start(ap, format);
 vsprintf(buf + strlen(buf), format, ap);
 va_end(ap);
}
static void jit_internal_cleanup(struct jit *jit)
{
 for (jit_op *op = jit_op_first(jit->ops); op; op = op->next) {
  if (op->live_in) {
   jit_set_free(op->live_in);
   op->live_in = NULL;
  }
  if (op->live_out) {
   jit_set_free(op->live_out);
   op->live_out = NULL;
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   if (op->arg[1]) {
    struct jit_func_info *info = (struct jit_func_info *)op->arg[1];
    free(info->args);
    info->args = NULL;
   }
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PREPARE) {
   op->arg[0] = 0;
   op->arg[1] = 0;
  }
 }
}
static int jit_internal_check_dead_code(jit_op *op, char *msg_buf)
{
 if (!op->in_use) {
  jit_internal_append_msg(msg_buf, "unreachable operation");
  return JIT_WARN_DEAD_CODE;
 }
 return 0;
}
static int jit_internal_check_missing_patches(jit_op *op, char *msg_buf)
{
 if ((((((jit_opcode) (op->code & 0xfff8)) == JIT_CALL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_JMP)) && (op->code & 0x02)) || jit_internal_is_cond_branch_op(op)) {
  if ((op->arg[0] == (jit_value) (NULL)) && (op->jmp_addr == NULL)) {
   jit_internal_append_msg(msg_buf, "missing patch");
   return JIT_WARN_MISSING_PATCH;
  }
 }
 return 0;
}
static int jit_internal_check_op_without_effect(jit_op *op, char *msg_buf)
{
 jit_opcode code = ((jit_opcode) (op->code & 0xfff8));
 if ((code == JIT_ADDC) || (code == JIT_ADDX) || (code == JIT_SUBC) || (code == JIT_SUBX)
 || (code == JIT_BOADD) || (code == JIT_BOSUB) || (code == JIT_BNOADD) || (code == JIT_BNOSUB)) return 0;
 for (int i = 0; i < 3; i++) {
  if (((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03) && (!jit_set_get(op->live_out, op->arg[i]))) {
   jit_internal_append_msg(msg_buf, "operation without effect");
   return JIT_WARN_OP_WITHOUT_EFFECT;
  }
 }
 return 0;
}
static void jit_internal_print_regs(jit_tree_key reg, jit_tree_value v, void *thunk)
{
 char buf[32];
 if (reg == (((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((0) & 0xfffffff) << 4))) return;
 jit_get_reg_name(&jit_debugging_disasm, buf, reg);
 strcat(thunk, " ");
 strcat(thunk, buf);
}
static int jit_internal_check_uninitialized_registers(jit_op *op, char *msg_buf)
{
 if (((jit_opcode) (op->code & 0xfff8)) != JIT_PROLOG) return 0;
 if (op->live_in->root != NULL) {
  char buf[4096];
  buf[0] = '\0';
  jit_tree_walk(op->live_in->root, jit_internal_print_regs, buf);
  if (strlen(buf)) {
   jit_internal_append_msg(msg_buf, "uninitialized register(s): %s", buf);
   return JIT_WARN_UNINITIALIZED_REG;
  }
 }
 return 0;
}
static int jit_internal_valid_size(int size) {
 switch (size) {
  case 1: case 2: case 4:
   return 1;
  default:
   return 0;
 }
}
static int jit_internal_valid_fsize(int size)
{
 return (size == 4) || (size == 8);
}
static int jit_internal_check_argument_sizes(jit_op *op, char *msg_buf)
{
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_LD: case JIT_LDX: case JIT_ST: case JIT_STX:
   if (jit_internal_valid_size(op->arg_size)) return 0;
   break;
  case JIT_FLD: case JIT_FLDX: case JIT_FST: case JIT_FSTX:
  case JIT_FPUTARG: case JIT_FRET: case JIT_FRETVAL:
   if (jit_internal_valid_fsize(op->arg_size)) return 0;
   break;
  case JIT_DECL_ARG:
   if (((op->arg[0] == JIT_SIGNED_NUM) || (op->arg[0] == JIT_UNSIGNED_NUM)) && jit_internal_valid_size(op->arg[1])) return 0;
   if ((op->arg[0] == JIT_FLOAT_NUM) && jit_internal_valid_fsize(op->arg[1])) return 0;
   if ((op->arg[0] == JIT_PTR) && (op->arg[1] == sizeof(void *))) return 0;
   break;
  default:
   return 0;
 }
 jit_internal_append_msg(msg_buf, "invalid data size");
 return JIT_WARN_INVALID_DATA_SIZE;
}
static int jit_internal_check_register_types(struct jit *jit, jit_op *op, char *msg_buf)
{
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_GETARG: {
   struct jit_func_info * info = jit_current_func_info(jit);
   if (info->args[op->arg[1]].type == JIT_FLOAT_NUM) {
    if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (1)))) return 0;
   } else {
    if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (0)))) return 0;
   }
   break;
  }
  case JIT_FST:
  case JIT_TRUNC:
  case JIT_CEIL:
  case JIT_ROUND:
  case JIT_FLOOR:
   if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (1)))) return 0;
   break;
  case JIT_EXT:
  case JIT_FLD:
   if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (1))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (0)))) return 0;
   break;
  case JIT_FLDX:
   if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (1))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[3 - 1]) & 0x01) == (0)))) return 0;
   break;
  case JIT_FSTX:
   if (((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[3 - 1]) & 0x01) == (1)))) return 0;
   break;
  case JIT_FORCE_SPILL:
  case JIT_FORCE_ASSOC:
   return 0;
  default:
   if (!op->fp && ((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (0))) && ((((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[3 - 1]) & 0x01) == (0)))) return 0;
   if (op->fp && ((((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((1) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[1 - 1]) & 0x01) == (1))) && ((((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((2) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[2 - 1]) & 0x01) == (1))) && ((((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x01) && ((((op)->spec >> ((3) - 1) * 2) & 0x03) != 0x03)) || (((op->arg[3 - 1]) & 0x01) == (1)))) return 0;
 }
 jit_internal_append_msg(msg_buf, "register type mismatch");
 return JIT_WARN_REGISTER_TYPE_MISMATCH;
}
static int jit_op_is_data_op(jit_op *op)
{
 while (op && ((((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH))) op = op->next;
 if (!op) return 0;
 jit_opcode code = ((jit_opcode) (op->code & 0xfff8));
 return ((code == JIT_DATA_BYTE) || (code == JIT_DATA_BYTES) || (code == JIT_DATA_REF_CODE) || (code == JIT_DATA_REF_DATA));
}
static int jit_internal_check_data_alignment(jit_op *op, char *msg_buf)
{
 if (jit_op_is_data_op(op) || (((jit_opcode) (op->code & 0xfff8)) == JIT_CODE_ALIGN)) return 0;
 if ((((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH)) return 0;
 jit_op * prev = op->prev;
 while (prev) {
  if ((((jit_opcode) (prev->code & 0xfff8)) == JIT_LABEL) || (((jit_opcode) (prev->code & 0xfff8)) == JIT_PATCH))
   prev = prev->prev;
  else break;
 }
 if (jit_op_is_data_op(prev)) {
  jit_internal_append_msg(msg_buf, "instruction follows unaligned data block");
  return JIT_WARN_UNALIGNED_CODE;
 }
 return 0;
}
static int jit_internal_check_data_references(jit_op *op, char *msg_buf)
{
 if (((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_DATA) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_DATA)) && !jit_op_is_data_op(op->jmp_addr)) {
  jit_internal_append_msg(msg_buf, "invalid data reference");
  return JIT_WARN_INVALID_DATA_REFERENCE;
 }
 return 0;
}
static int jit_internal_check_code_references(jit_op *op, char *msg_buf)
{
 if (((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE)) && jit_op_is_data_op(op->jmp_addr)) {
  jit_internal_append_msg(msg_buf, "invalid code reference");
  return JIT_WARN_INVALID_CODE_REFERENCE;
 }
 return 0;
}
void jit_check_code(struct jit *jit, int warnings)
{
 char buf[8192];
 jit_expand_patches_and_labels(jit);
 jit_dead_code_analysis(jit, 0);
 jit_prepare_reg_counts(jit);
        jit_prepare_arguments(jit);
 jit_flw_analysis(jit);
 for (jit_op *op = jit_op_first(jit->ops); op; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) jit->current_func = op;
  if (!op->debug_info) continue;
  buf[0] = '\0';
  if (warnings & JIT_WARN_DEAD_CODE) op->debug_info->warnings |= jit_internal_check_dead_code(op, buf);
  if (warnings & JIT_WARN_MISSING_PATCH) op->debug_info->warnings |= jit_internal_check_missing_patches(op, buf);
  if (warnings & JIT_WARN_OP_WITHOUT_EFFECT) op->debug_info->warnings |= jit_internal_check_op_without_effect(op, buf);
  if (warnings & JIT_WARN_UNINITIALIZED_REG) op->debug_info->warnings |= jit_internal_check_uninitialized_registers(op, buf);
  if (warnings & JIT_WARN_INVALID_DATA_SIZE) op->debug_info->warnings |= jit_internal_check_argument_sizes(op, buf);
  if (warnings & JIT_WARN_REGISTER_TYPE_MISMATCH) op->debug_info->warnings |= jit_internal_check_register_types(jit, op, buf);
  if (warnings & JIT_WARN_UNALIGNED_CODE) op->debug_info->warnings |= jit_internal_check_data_alignment(op, buf);
  if (warnings & JIT_WARN_INVALID_DATA_REFERENCE) op->debug_info->warnings |= jit_internal_check_data_references(op, buf);
  if (warnings & JIT_WARN_INVALID_CODE_REFERENCE) op->debug_info->warnings |= jit_internal_check_code_references(op, buf);
  if (op->debug_info->warnings) jit_internal_report_warning(jit, op, buf);
 }
 jit_internal_cleanup(jit);
}
static inline void jit_flw_initialize(struct jit * jit)
{
 struct jit_func_info *func_info;
 jit_op * op = jit_op_first(jit->ops);
 while (op) {
  op->live_in = jit_set_new();
  op->live_out = jit_set_new();
  for (int i = 0; i < 3; i++)
   if ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01)
    jit_set_add(op->live_in, op->arg[i]);
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   func_info = (struct jit_func_info *)op->arg[1];
  }
  op = op->next;
 }
}
static inline void jit_internal_flw_analyze_prolog(struct jit * jit, jit_op * op, struct jit_func_info * func_info)
{
}
struct code_refs_cache {
 int size;
 jit_op **ops;
};
static inline void jit_internal_initialize_code_refs(struct code_refs_cache *code_refs, struct jit_func_info *func_info)
{
 jit_op *op = func_info->first_op->next;
 code_refs->size = 0;
 while (op && (((jit_opcode) (op->code & 0xfff8)) != JIT_PROLOG)) {
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE))
   code_refs->size++;
  op = op->next;
 }
 code_refs->ops = malloc(sizeof(jit_op *) * code_refs->size);
 op = func_info->first_op->next;
 int i = 0;
 while (op && (((jit_opcode) (op->code & 0xfff8)) != JIT_PROLOG)) {
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE))
   code_refs->ops[i++] = op;
  op = op->next;
 }
}
static inline int jit_internal_flw_analyze_op(struct jit * jit, jit_op * op, struct jit_func_info * func_info, int changed, struct code_refs_cache *code_refs)
{
 int live_out_size = jit_set_size(op->live_out);
 int live_in_size = jit_set_size(op->live_in);
 if (op->jmp_addr && (((jit_opcode) (op->code & 0xfff8)) != JIT_REF_CODE) && (((jit_opcode) (op->code & 0xfff8)) != JIT_DATA_REF_CODE))
  jit_set_addall(op->live_out, op->jmp_addr->live_in);
 if (op->code == (JIT_JMP | 0x01)) {
  if (code_refs->size < 0) jit_internal_initialize_code_refs(code_refs, func_info);
  for (int i = 0; i < code_refs->size; i++) {
   jit_set_addall(op->live_out, code_refs->ops[i]->jmp_addr->live_in);
  }
  goto skip;
 }
 if (op->code == (JIT_JMP | 0x02)) goto skip;
 if (op->next) jit_set_addall(op->live_out, op->next->live_in);
skip:
 jit_set_addall(op->live_in, op->live_out);
 for (int i = 0; i < 3; i++)
  if ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03) jit_set_remove(op->live_in, op->arg[i]);
 for (int i = 0; i < 3; i++)
  if ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01) jit_set_add(op->live_in, op->arg[i]);
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) jit_internal_flw_analyze_prolog(jit, op, func_info);
 if (changed) return changed;
 if (live_out_size != jit_set_size(op->live_out)) return 1;
 if (live_in_size != jit_set_size(op->live_in)) return 1;
 return 0;
}
static inline void jit_internal_analyze_function(struct jit *jit, jit_op *first_op, jit_op *last_op)
{
 int changed;
 struct code_refs_cache code_refs = { -1, NULL };
 struct jit_func_info * func_info = (struct jit_func_info *)first_op->arg[1];
 do {
  changed = 0;
  jit_op * op = last_op;
  while (1) {
   changed |= jit_internal_flw_analyze_op(jit, op, func_info, changed, &code_refs);
   if (op == first_op) break;
   op = op->prev;
  }
 } while (changed);
 if (code_refs.ops) free(code_refs.ops);
}
static inline void jit_flw_analysis(struct jit * jit)
{
 jit_flw_initialize(jit);
 jit_op *op = jit_op_first(jit->ops);
 while (op) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   jit_op *first = op;
   while (1) {
    if ((op->next == NULL) || (((jit_opcode) (op->next->code & 0xfff8)) == JIT_PROLOG)) {
     jit_op *second = op;
     jit_internal_analyze_function(jit, first, second);
     break;
    }
    op = op->next;
   }
  }
  op = op->next;
 }
}
static inline void jit_internal_mark_livecode(jit_op *op)
{
 while (op) {
  if (op->in_use) return;
  op->in_use = 1;
  if (op->jmp_addr) jit_internal_mark_livecode(op->jmp_addr);
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_RET) return;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FRET) return;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_JMP) return;
  op = op->next;
 }
}
static void jit_dead_code_analysis(struct jit *jit, int remove_dead_code)
{
 for (jit_op *op = jit_op_first(jit->ops); op; op = op->next)
  op->in_use = 0;
 for (jit_op *op = jit_op_first(jit->ops); op; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) jit_internal_mark_livecode(op);
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE) jit_internal_mark_livecode(op->jmp_addr);
 }
 for (jit_op *op = jit_op_first(jit->ops); op; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_CODESTART) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTE) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_DATA) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_CODE_ALIGN) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_COMMENT) op->in_use = 1;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_MARK) op->in_use = 1;
 }
 if (!remove_dead_code) return;
 jit_op *op = jit_op_first(jit->ops);
 while (op) {
  if (!op->in_use) {
   if (((jit_opcode) (op->code & 0xfff8)) == JIT_FULL_SPILL) goto skip;
   jit_op *next = op->next;
   jit_op_delete(op);
   op = next;
   continue;
  }
skip:
  op = op->next;
 }
}
static inline void jit_internal_unload_reg(jit_op * op, jit_hw_reg * hreg, long virt_reg);
static inline void jit_internal_load_reg(struct jit_op * op, jit_hw_reg * hreg, long reg);
static inline jit_rmap * jit_internal_rmap_init()
{
 jit_rmap * res = malloc(sizeof(jit_rmap));
 res->map = NULL;
 return res;
}
jit_hw_reg * jit_internal_rmap_get(jit_rmap * rmap, jit_value reg)
{
 jit_tree * found = jit_tree_search(rmap->map, reg);
 if (found) return (jit_hw_reg *) found->value;
 return NULL;
}
static inline jit_hw_reg * jit_internal_rmap_is_associated_aux(jit_tree * n, int reg_id, int fp, jit_value * virt_reg)
{
 if (n == NULL) return NULL;
 jit_hw_reg * r = (jit_hw_reg *) n->value;
 if ((r->fp == fp) && (r->id == reg_id)) {
  if (virt_reg) *virt_reg = (jit_value) n->key;
  return r;
 }
 r = jit_internal_rmap_is_associated_aux(n->left, reg_id, fp, virt_reg);
 if (r) return r;
 else return jit_internal_rmap_is_associated_aux(n->right, reg_id, fp, virt_reg);
}
static jit_hw_reg * jit_internal_rmap_is_associated(jit_rmap * rmap, int reg_id, int fp, jit_value * virt_reg)
{
 return jit_internal_rmap_is_associated_aux(rmap->map, reg_id, fp, virt_reg);
}
static void jit_internal_rmap_assoc(jit_rmap * rmap, jit_value reg, jit_hw_reg * hreg)
{
 rmap->map = jit_tree_insert(rmap->map, reg, hreg, NULL);
}
static void jit_internal_rmap_unassoc(jit_rmap * rmap, jit_value reg)
{
 rmap->map = jit_tree_delete(rmap->map, reg, NULL);
}
static jit_rmap * jit_internal_rmap_clone(jit_rmap * rmap)
{
 jit_rmap * res = malloc(sizeof(jit_rmap));
 res->map = jit_tree_clone(rmap->map);
 return res;
}
static int jit_internal_rmap_subset(jit_op * op, jit_tree * current, jit_tree * target)
{
 if (current == NULL) return 1;
 jit_set * tgt_livein = op->jmp_addr->live_in;
 if (!jit_set_get(tgt_livein, current->key)) goto skip;
 jit_tree * found = jit_tree_search(target, current->key);
 if ((!found) || (current->value != found->value)) return 0;
skip:
 return jit_internal_rmap_subset(op, current->left, target) && jit_internal_rmap_subset(op, current->right, target);
}
static int jit_internal_rmap_equal(jit_op * op, jit_rmap * current, jit_rmap * target)
{
 return jit_internal_rmap_subset(op, current->map, target->map) && jit_internal_rmap_subset(op, target->map, current->map);
}
static void jit_internal_rmap_sync_aux(jit_tree * current, jit_tree * target, jit_op * op, int mode)
{
 if (current == NULL) return;
 if ((mode == (2)) && (!jit_set_get(op->live_out, current->key))) goto skip;
 if ((mode == (1)) && (!jit_set_get(op->jmp_addr->live_in, current->key))) goto skip;
 jit_tree * found = jit_tree_search(target, current->key);
 int i = current->key;
 if ((!found) || (current->value != found->value)) {
  jit_hw_reg * hreg = (jit_hw_reg *) current->value;
  switch (mode) {
   case (1): jit_internal_unload_reg(op, hreg, i); break;
   case (2): jit_internal_load_reg(op, hreg, i); break;
   default: assert(0);
  }
 }
skip:
 jit_internal_rmap_sync_aux(current->left, target, op, mode);
 jit_internal_rmap_sync_aux(current->right, target, op, mode);
}
static void jit_internal_rmap_sync(jit_op * op, jit_rmap * current, jit_rmap * target, int mode)
{
 jit_internal_rmap_sync_aux(current->map, target->map, op, mode);
}
static int jit_internal_candidate_score(jit_op * op, jit_value virtreg, jit_hw_reg * hreg, int * spill, jit_value * associated_virtreg)
{
 int score = 0;
 score -= hreg->priority;
 jit_value x;
 int hw_associated = (jit_internal_rmap_is_associated(op->regmap, hreg->id, hreg->fp, &x) != NULL);
 int alive = 0;
 if (hw_associated) {
  alive = (jit_set_get(op->live_in, x) || jit_set_get(op->live_out, x));
 }
 if (!alive) score += 10000;
 *spill = 0;
 if (hw_associated) {
  score -= 100000;
  *spill = 1;
  *associated_virtreg = x;
  jit_tree * hint_node = jit_tree_search(op->allocator_hints, x);
  int is_to_be_used = (hint_node != NULL);
  if (!is_to_be_used) score += 50000;
  else {
   struct jit_allocator_hint * hint = (struct jit_allocator_hint *)hint_node->value;
   int used_in_steps = -(hint->last_pos - op->normalized_pos);
   if (hw_associated && (used_in_steps == 0)) return INT_MIN;
   else score += (used_in_steps * 5);
  }
 }
 jit_tree * hint_node = jit_tree_search(op->allocator_hints, virtreg);
 if (hint_node) {
  struct jit_allocator_hint * hint = (struct jit_allocator_hint *)hint_node->value;
  if ((hreg->fp == 0) && (hreg->id == X86_EAX)) {
   score += hint->should_be_eax * 5;
  }
  if (hreg->callee_saved) score += (hint->should_be_calleesaved - 1) * 15;
 }
 return score;
}
static jit_hw_reg * jit_internal_rmap_spill_candidate(struct jit_reg_allocator * al, jit_op * op, jit_value virtreg, int * spill, jit_value * reg_to_spill, int callee_saved)
{
 jit_reg r = (jit_reg) virtreg;
 jit_hw_reg * regs;
 int reg_count;
 jit_hw_reg * result = NULL;
 int best_score = INT_MIN;
 if (((r) & 0x01) == (0)) {
  regs = al->gp_regs;
  reg_count = al->gp_reg_cnt;
 } else {
  regs = al->fp_regs;
  reg_count = al->fp_reg_cnt;
 }
 int sp = 0;
 for (int i = 0; i < reg_count; i++) {
  if (callee_saved && !regs[i].callee_saved) continue;
  jit_value assoc = 0;
  int score = jit_internal_candidate_score(op, virtreg, &(regs[i]), &sp, &assoc);
  if (score > best_score) {
   if (sp) {
    *reg_to_spill = assoc;
    *spill = sp;
   } else {
    *reg_to_spill = -1;
    *spill = 0;
   }
   result = &(regs[i]);
   best_score = score;
  }
 }
 return result;
}
void jit_internal_rmap_free(jit_rmap * regmap)
{
 if (!regmap) return;
 jit_tree_free(regmap->map);
 free(regmap);
}
static void jit_internal_insert_reg_op(int opcode, jit_op * op, jit_value r1, jit_value r2)
{
 jit_op * o = jit_op_new(opcode, (((0x00) << 4) | ((0x02) << 2) | (0x02)), r1, r2, 0, 0);
 o->r_arg[0] = o->arg[0];
 o->r_arg[1] = o->arg[1];
 jit_op_prepend(op, o);
}
static void jit_internal_unload_reg(jit_op * op, jit_hw_reg * hreg, jit_value virt_reg)
{
 jit_internal_insert_reg_op(JIT_UREG, op, virt_reg, hreg->id);
}
static void jit_internal_sync_reg(jit_op * op, jit_hw_reg * hreg, jit_value virt_reg)
{
 jit_internal_insert_reg_op(JIT_SYNCREG, op, virt_reg, hreg->id);
}
static void jit_internal_load_reg(jit_op * op, jit_hw_reg * hreg, jit_value reg)
{
 jit_internal_insert_reg_op(JIT_LREG, op, hreg->id, reg);
}
static void jit_internal_rename_reg(jit_op * op, int r1, int r2)
{
 jit_internal_insert_reg_op(JIT_RENAMEREG, op, r1, r2);
}
static jit_hw_reg * jit_internal_make_free_reg(struct jit_reg_allocator * al, jit_op * op, jit_value for_reg)
{
 int spill = 0;
 jit_value spill_candidate = -1;
 jit_hw_reg * hreg = jit_internal_rmap_spill_candidate(al, op, for_reg, &spill, &spill_candidate, 0);
 if (spill) {
  if (jit_set_get(op->live_in, spill_candidate))
   jit_internal_unload_reg(op, hreg, spill_candidate);
  jit_internal_rmap_unassoc(op->regmap, spill_candidate);
 }
 return hreg;
}
static void jit_internal_assign_regs_for_args(struct jit_reg_allocator * al, jit_op * op)
{
 struct jit_func_info * info = (struct jit_func_info *) op->arg[1];
 int assoc_gp_regs = 0;
 int assoc_fp_regs = 0;
 for (int i = 0; i < info->general_arg_cnt + info->float_arg_cnt; i++) {
  int isfp_arg = (info->args[i].type == JIT_FLOAT_NUM);
  if (!isfp_arg && (assoc_gp_regs < al->gp_arg_reg_cnt)) {
   jit_internal_rmap_assoc(op->regmap, ((((0)) & 0x01) | ((((3)) & 0x03) << 1) | ((i) & 0xfffffff) << 4), al->gp_arg_regs[assoc_gp_regs]);
   assoc_gp_regs++;
  }
  if (isfp_arg && (assoc_fp_regs < al->fp_arg_reg_cnt)) {
   jit_internal_rmap_assoc(op->regmap, ((((1)) & 0x01) | ((((3)) & 0x03) << 1) | ((i) & 0xfffffff) << 4), al->fp_arg_regs[assoc_fp_regs]);
   assoc_fp_regs++;
  }
 }
}
static void jit_internal_prepare_registers_for_call(struct jit_reg_allocator * al, jit_op * op)
{
 jit_value r, reg;
 jit_hw_reg * hreg = NULL;
 if (al->ret_reg) hreg = jit_internal_rmap_is_associated(op->regmap, al->ret_reg->id, 0, &r);
 if (hreg) {
  int alive = (jit_set_get(op->live_out, r) || (jit_set_get(op->live_in, r)));
  if (!alive) goto skip;
  int spill;
  jit_value spill_reg;
  jit_hw_reg * freereg = jit_internal_rmap_spill_candidate(al, op, r, &spill, &spill_reg, 1);
  if (freereg && !spill) {
   jit_internal_rename_reg(op, freereg->id, al->ret_reg->id);
   jit_internal_rmap_unassoc(op->regmap, r);
   jit_internal_rmap_assoc(op->regmap, r, freereg);
  } else {
   jit_internal_sync_reg(op, hreg, r);
  }
 }
skip:
 if (al->fpret_reg) {
  hreg = jit_internal_rmap_is_associated(op->regmap, al->fpret_reg->id, 1, &r);
  if (hreg) jit_internal_sync_reg(op, hreg, r);
 }
 int args = ((op->arg[0]) < (al->gp_arg_reg_cnt) ? (op->arg[0]) : (al->gp_arg_reg_cnt));
 for (int q = 0; q < args; q++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->gp_arg_regs[q]->id, 0, &reg);
  if (hreg) {
   if (jit_set_get(op->live_out, reg)) jit_internal_unload_reg(op, hreg, reg);
   jit_internal_rmap_unassoc(op->regmap, reg);
  }
 }
 args = ((op->arg[1]) < (al->fp_arg_reg_cnt) ? (op->arg[1]) : (al->fp_arg_reg_cnt));
 for (int q = 0; q < args; q++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->fp_arg_regs[q]->id, 1, &reg);
  if (hreg) {
   if ((hreg->id != al->fpret_reg->id) && jit_set_get(op->live_out, reg)) jit_internal_unload_reg(op, hreg, reg);
   jit_internal_rmap_unassoc(op->regmap, reg);
  }
 }
}
static int jit_internal_assign_ret_reg(jit_op * op, jit_hw_reg * ret_reg)
{
 jit_internal_rmap_assoc(op->regmap, op->arg[0], ret_reg);
 return 1;
}
static int jit_internal_assign_getarg(jit_op * op, struct jit_reg_allocator * al)
{
 int arg_id = op->arg[1];
 struct jit_inp_arg * arg = &(al->current_func_info->args[arg_id]);
 int reg_id = (((arg->type == JIT_FLOAT_NUM ? (1) : (0)) & 0x01) | ((((3)) & 0x03) << 1) | ((arg_id) & 0xfffffff) << 4);
 if (!jit_set_get(op->live_out, reg_id)) {
  if ((arg->type != JIT_FLOAT_NUM) && (arg->size == (sizeof(void *))))
  {
   jit_hw_reg * hreg = jit_internal_rmap_get(op->regmap, reg_id);
   if (hreg) {
    jit_internal_rmap_unassoc(op->regmap, reg_id);
    jit_internal_rmap_assoc(op->regmap, op->arg[0], hreg);
    op->r_arg[0] = hreg->id;
    op->r_arg[1] = op->arg[1];
    op->code = JIT_NOP;
    return 1;
   }
  }
 }
 return 0;
}
static void jit_internal_spill_ret_retreg(jit_op * op, jit_hw_reg * ret_reg)
{
 jit_value r;
 if (ret_reg) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, ret_reg->id, ret_reg->fp, &r);
  if (hreg) jit_internal_rmap_unassoc(op->regmap, r);
 }
}
static int jit_internal_assign_jmp(jit_op * op, struct jit_reg_allocator * al)
{
 if (op->code == (JIT_JMP | 0x02)) return 0;
 jit_value reg;
 for (int i = 0; i < al->gp_reg_cnt; i++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->gp_regs[i].id, 0, &reg);
  if (hreg && jit_set_get(op->live_out, reg)) jit_internal_sync_reg(op, hreg, reg);
 }
 for (int i = 0; i < al->fp_reg_cnt; i++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->fp_regs[i].id, 1, &reg);
  if (hreg && jit_set_get(op->live_out, reg)) jit_internal_sync_reg(op, hreg, reg);
 }
 return 0;
}
static int jit_internal_assign_call(jit_op * op, struct jit_reg_allocator * al)
{
 jit_internal_spill_ret_retreg(op, al->ret_reg);
 jit_internal_spill_ret_retreg(op, al->fpret_reg);
 return 0;
}
static int jit_internal_spill_all_registers(jit_op *op, struct jit_reg_allocator * al)
{
 jit_value reg;
 for (int i = 0; i < al->gp_reg_cnt; i++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->gp_regs[i].id, 0, &reg);
  if (hreg && (jit_set_get(op->live_out, reg))) {
   if (op->in_use) jit_internal_unload_reg(op, hreg, reg);
   jit_internal_rmap_unassoc(op->regmap, reg);
  }
 }
 for (int i = 0; i < al->fp_reg_cnt; i++) {
  jit_hw_reg * hreg = jit_internal_rmap_is_associated(op->regmap, al->fp_regs[i].id, 1, &reg);
  if (hreg && (jit_set_get(op->live_out, reg))) {
   if (op->in_use) jit_internal_unload_reg(op, hreg, reg);
   jit_internal_rmap_unassoc(op->regmap, reg);
  }
 }
 return 1;
}
static int jit_internal_force_spill(jit_op *op)
{
 jit_value reg = op->arg[0];
 jit_hw_reg *hreg = jit_internal_rmap_get(op->regmap, reg);
 if (hreg) {
  jit_internal_unload_reg(op, hreg, reg);
  jit_internal_rmap_unassoc(op->regmap, reg);
 }
 return 1;
}
static int jit_internal_force_assoc(jit_op *op, struct jit_reg_allocator *al)
{
 jit_hw_reg *hreg = (op->arg[1] == 0 ? &al->gp_regs[op->arg[2]] : &al->fp_regs[op->arg[2]]);
 jit_internal_rmap_assoc(op->regmap, op->arg[0], hreg);
 jit_internal_load_reg(op, hreg, op->arg[0]);
 return 1;
}
static void jit_internal_associate_register_alias(struct jit_reg_allocator * al, jit_op * op, int i)
{
 if ((int)op->arg[i] == (int)(((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((1) & 0xfffffff) << 4))) op->r_arg[i] = al->ret_reg->id;
 else if ((int)op->arg[i] == (int)(((((0)) & 0x01) | ((((2)) & 0x03) << 1) | ((0) & 0xfffffff) << 4))) op->r_arg[i] = al->fp_reg;
 else assert(0);
}
static int jit_internal_is_transfer_op(jit_op *op)
{
 jit_opcode code = ((jit_opcode) (op->code & 0xfff8));
 return (code == JIT_TRANSFER_ADD)
  || (code == JIT_TRANSFER_SUB)
  || (code == JIT_TRANSFER_OR)
  || (code == JIT_TRANSFER_XOR)
  || (code == JIT_TRANSFER_AND);
}
static void jit_internal_associate_register(struct jit_reg_allocator * al, jit_op * op, int i)
{
 jit_hw_reg * reg = jit_internal_rmap_get(op->regmap, op->arg[i]);
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_FRETVAL) printf(":JJJ:%i\n", reg->id);
 if (reg) op->r_arg[i] = reg->id;
 else {
  if (!jit_internal_is_transfer_op(op)
  ) {
   reg = jit_internal_make_free_reg(al, op, op->arg[i]);
   jit_internal_rmap_assoc(op->regmap, op->arg[i], reg);
   op->r_arg[i] = reg->id;
   if (jit_set_get(op->live_in, op->arg[i]))
    jit_internal_load_reg(op, jit_internal_rmap_get(op->regmap, op->arg[i]), op->arg[i]);
  } else op->r_arg[i] = -1;
 }
}
static void jit_internal_assign_regs(struct jit * jit, struct jit_op * op)
{
 int i;
 int skip = 0;
 struct jit_reg_allocator * al = jit->reg_al;
 if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
  struct jit_func_info * info = (struct jit_func_info *) op->arg[1];
  al->current_func_info = info;
  jit_internal_assign_regs_for_args(al, op);
 } else {
  if (op->prev) {
   jit_internal_rmap_free(op->regmap);
   op->regmap = jit_internal_rmap_clone(op->prev->regmap);
  }
 }
 switch (((jit_opcode) (op->code & 0xfff8))) {
  case JIT_PREPARE: jit_internal_prepare_registers_for_call(al, op); break;
  case JIT_PUTARG: skip = 1; break;
  case JIT_FPUTARG: skip = 1; break;
  case JIT_RETVAL: skip = jit_internal_assign_ret_reg(op, al->ret_reg); break;
  case JIT_GETARG: skip = jit_internal_assign_getarg(op, al); break;
  case JIT_CALL: skip = jit_internal_assign_call(op, al); break;
  case JIT_JMP: skip = jit_internal_assign_jmp(op, al); break;
  case JIT_FULL_SPILL: skip = jit_internal_spill_all_registers(op, al); break;
  case JIT_FORCE_SPILL: skip = jit_internal_force_spill(op); break;
  case JIT_FORCE_ASSOC: skip = jit_internal_force_assoc(op, al); break;
  default: break;
 }
 if (skip) return;
 for (i = 0; i < 3; i++) {
  if (((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01) || ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03)) {
   jit_reg virt_reg = (jit_reg) op->arg[i];
   if ((((virt_reg) >> 1) & 0x03) == (2)) jit_internal_associate_register_alias(al, op, i);
   else jit_internal_associate_register(al, op, i);
  } else if ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x02) {
   op->r_arg[i] = op->arg[i];
  }
 }
}
static void jit_internal_mark_calleesaved_regs(jit_tree * hint, jit_op * op)
{
 if (hint == NULL) return;
 struct jit_allocator_hint * h = (struct jit_allocator_hint *) hint->value;
 jit_value reg = (jit_value) hint->key;
 if (jit_set_get(op->live_out, reg)) h->should_be_calleesaved++;
 jit_internal_mark_calleesaved_regs(hint->left, op);
 jit_internal_mark_calleesaved_regs(hint->right, op);
}
static void jit_internal_hints_refcount_inc(jit_tree * hints);
void jit_collect_statistics(struct jit * jit)
{
 int i, j;
 int ops_from_return = 0;
 jit_tree * last_hints = NULL;
 for (jit_op * op = jit_op_last(jit->ops); op != NULL; op = op->prev) {
  jit_tree * new_hints = jit_tree_clone(last_hints);
  op->normalized_pos = ops_from_return;
  jit_value regs[3];
  int found_regs = 0;
  for (i = 0; i < 3; i++)
   if (((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01) || ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03)) {
    int found = 0;
    jit_value reg = op->arg[i];
    for (j = 0; j < found_regs; j++) {
     if (regs[j] == reg) {
      found = 1;
      break;
     }
    }
    if (!found) regs[found_regs++] = reg;
   }
  for (i = 0; i < found_regs; i++) {
   jit_value reg = regs[i];
   jit_tree * hint = jit_tree_search(new_hints, reg);
   struct jit_allocator_hint * new_hint = malloc(sizeof(struct jit_allocator_hint));
   if (hint) memcpy(new_hint, hint->value, sizeof(struct jit_allocator_hint));
   else {
    new_hint->last_pos = 0;
    new_hint->should_be_calleesaved = 0;
    new_hint->should_be_eax = 0;
   }
   new_hint->refs = 0;
   new_hint->last_pos = ops_from_return;
   if ((((jit_opcode) (op->code & 0xfff8)) == JIT_RETVAL) || (((jit_opcode) (op->code & 0xfff8)) == JIT_RET))
    new_hint->should_be_eax++;
   new_hints = jit_tree_insert(new_hints, reg, new_hint, NULL);
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_CALL) jit_internal_mark_calleesaved_regs(new_hints, op);
  jit_internal_hints_refcount_inc(new_hints);
  op->allocator_hints = new_hints;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   last_hints = NULL;
   ops_from_return = 0;
  } else {
   last_hints = new_hints;
   ops_from_return++;
  }
 }
}
static void jit_internal_hints_refcount_inc(jit_tree * hints)
{
 if (hints == NULL) return;
 ((struct jit_allocator_hint*) hints->value)->refs++;
 jit_internal_hints_refcount_inc(hints->left);
 jit_internal_hints_refcount_inc(hints->right);
}
void jit_allocator_hints_free(jit_tree * hints)
{
 if (hints == NULL) return;
 jit_allocator_hints_free(hints->left);
 jit_allocator_hints_free(hints->right);
 int refs = --((struct jit_allocator_hint*) hints->value)->refs;
 if (refs == 0) free(hints->value);
 free(hints);
}
static inline void jit_internal_jump_adjustment(struct jit * jit, jit_op * op)
{
 if (op->code == (JIT_JMP | 0x02)) {
  jit_rmap * cur_regmap = op->regmap;
  jit_rmap * tgt_regmap = op->jmp_addr->regmap;
  jit_internal_rmap_sync(op, cur_regmap, tgt_regmap, (1));
  jit_internal_rmap_sync(op, tgt_regmap, cur_regmap, (2));
 }
}
static inline void jit_internal_branch_adjustment(struct jit * jit, jit_op * op)
{
 if (!jit_internal_is_cond_branch_op(op)) return;
 jit_rmap * cur_regmap = op->regmap;
 jit_rmap * tgt_regmap = op->jmp_addr->regmap;
 if (!jit_internal_rmap_subset(op, tgt_regmap->map, cur_regmap->map)) {
  switch (((jit_opcode) (op->code & 0xfff8))) {
   case JIT_BEQ: op->code = JIT_BNE | (op->code & 0x7); break;
   case JIT_BGT: op->code = JIT_BLE | (op->code & 0x7); break;
   case JIT_BGE: op->code = JIT_BLT | (op->code & 0x7); break;
   case JIT_BNE: op->code = JIT_BEQ | (op->code & 0x7); break;
   case JIT_BLT: op->code = JIT_BGE | (op->code & 0x7); break;
   case JIT_BLE: op->code = JIT_BGT | (op->code & 0x7); break;
   case JIT_BOADD: op->code = JIT_BNOADD | (op->code & 0x7); break;
   case JIT_BOSUB: op->code = JIT_BNOSUB | (op->code & 0x7); break;
   case JIT_BNOADD: op->code = JIT_BOADD | (op->code & 0x7); break;
   case JIT_BNOSUB: op->code = JIT_BOSUB | (op->code & 0x7); break;
   case JIT_FBEQ: op->code = JIT_FBNE | (op->code & 0x7); break;
   case JIT_FBGT: op->code = JIT_FBLE | (op->code & 0x7); break;
   case JIT_FBGE: op->code = JIT_FBLT | (op->code & 0x7); break;
   case JIT_FBNE: op->code = JIT_FBEQ | (op->code & 0x7); break;
   case JIT_FBLT: op->code = JIT_FBGE | (op->code & 0x7); break;
   case JIT_FBLE: op->code = JIT_FBGT | (op->code & 0x7); break;
   default: break;
  }
  jit_op * o = jit_op_new(JIT_JMP | 0x02, (((0x00) << 4) | ((0x00) << 2) | (0x02)), op->arg[0], 0, 0, 0);
  o->r_arg[0] = op->r_arg[0];
  o->regmap = jit_internal_rmap_clone(op->regmap);
  o->live_in = jit_set_clone(op->live_in);
  o->live_out = jit_set_clone(op->live_out);
  o->jmp_addr = op->jmp_addr;
  if (!jit_is_label(jit, (void *)op->r_arg[0])) {
   op->jmp_addr->arg[0] = (jit_value) o;
   op->jmp_addr->r_arg[0] = (jit_value) o;
  }
  jit_op_append(op, o);
  jit_op * o2 = jit_op_new(JIT_PATCH, (((0x00) << 4) | ((0x00) << 2) | (0x02)), (jit_value) op, 0, 0, 0);
  o2->r_arg[0] = o2->arg[0];
  jit_op_append(o, o2);
  op->arg[0] = (jit_value) o2;
  op->r_arg[0] = (jit_value) o2;
  op->jmp_addr = o2;
 }
}
void jit_assign_regs(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next)
  op->regmap = jit_internal_rmap_init();
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next)
  jit_internal_assign_regs(jit, op);
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next)
  jit_internal_branch_adjustment(jit, op);
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next)
  jit_internal_jump_adjustment(jit, op);
}
void jit_reg_allocator_free(struct jit_reg_allocator * a)
{
 if (a->fp_regs) free(a->fp_regs);
 free(a->gp_regs);
 if (a->fp_arg_regs) free(a->fp_arg_regs);
 if (a->gp_arg_regs) free(a->gp_arg_regs);
 free(a);
}
int jit_reg_in_use(jit_op * op, int reg, int fp)
{
 jit_value virt_reg;
 if (jit_internal_rmap_is_associated(op->regmap, reg, fp, &virt_reg)
 && ((jit_set_get(op->live_in, virt_reg) || (jit_set_get(op->live_out, virt_reg))))) return 1;
 else return 0;
}
jit_hw_reg * jit_get_unused_reg_with_index(struct jit_reg_allocator * al, jit_op * op, int fp, int index)
{
 jit_hw_reg * regs;
 int reg_count;
 if (!fp) {
  regs = al->gp_regs;
  reg_count = al->gp_reg_cnt;
 } else {
  regs = al->fp_regs;
  reg_count = al->fp_reg_cnt;
 }
 for (int i = 0; i < reg_count; i++) {
  if (regs[i].callee_saved) continue;
  if (!jit_reg_in_use(op, regs[i].id, fp)) {
   if (index == 0) return &(regs[i]);
   else index--;
  }
 }
 return NULL;
}
jit_hw_reg * jit_get_unused_reg(struct jit_reg_allocator * al, jit_op * op, int fp)
{
 return jit_get_unused_reg_with_index(al, op, fp, 0);
}
struct jit_op * jit_add_op(struct jit * jit, unsigned short code, unsigned char spec, long arg1, long arg2, long arg3, unsigned char arg_size, struct jit_debug_info *debug_info)
{
 struct jit_op * r = jit_op_new(code, spec, arg1, arg2, arg3, arg_size);
 r->debug_info = debug_info;
 jit_op_append(jit->last_op, r);
 jit->last_op = r;
 return r;
}
struct jit_op * jit_add_fop(struct jit * jit, unsigned short code, unsigned char spec, long arg1, long arg2, long arg3, double flt_imm, unsigned char arg_size, struct jit_debug_info *debug_info)
{
 struct jit_op * r = jit_add_op(jit, code, spec, arg1, arg2, arg3, arg_size, debug_info);
 r->fp = 1;
 r->flt_imm = flt_imm;
 return r;
}
struct jit_debug_info *jit_debug_info_new(const char *filename, const char *function, int lineno)
{
 struct jit_debug_info *r = malloc(sizeof(struct jit_debug_info));
 r->filename = filename;
 r->function = function;
 r->lineno = lineno;
 r->warnings = 0;
 return r;
}
struct jit * jit_init()
{
 struct jit * r = malloc(sizeof(struct jit));
 r->ops = jit_op_new(JIT_CODESTART, (((0x00) << 4) | ((0x00) << 2) | (0x00)), 0, 0, 0, 0);
 r->last_op = r->ops;
 r->optimizations = 0;
 r->buf = NULL;
 r->mmaped_buf = 0;
 r->labels = NULL;
 r->reg_al = jit_reg_allocator_create();
 jit_enable_optimization(r, (0x04) | (0x01) | (0x08));
 return r;
}
jit_op *jit_add_prolog(struct jit * jit, void * func, struct jit_debug_info *debug_info)
{
        jit_op * op = jit_add_op(jit, JIT_PROLOG , (((0x00) << 4) | ((0x00) << 2) | (0x02)), (long)func, 0, 0, 0, NULL);
        struct jit_func_info * info = malloc(sizeof(struct jit_func_info));
        op->arg[1] = (long)info;
 op->debug_info = debug_info;
        jit->current_func = op;
 info->first_op = op;
        info->allocai_mem = 0;
        info->general_arg_cnt = 0;
        info->float_arg_cnt = 0;
 return op;
}
jit_label * jit_get_label(struct jit * jit)
{
        jit_label * r = malloc(sizeof(jit_label));
        jit_add_op(jit, JIT_LABEL, (((0x00) << 4) | ((0x00) << 2) | (0x02)), (long)r, 0, 0, 0, NULL);
        r->next = jit->labels;
        jit->labels = r;
        return r;
}
static inline void jit_correct_float_imms(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if (!(op->code & 0x02)) continue;
  if (!op->fp) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FMOV) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FPUTARG) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FLD) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FLDX) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FST) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_FSTX) continue;
  int imm_arg;
  for (int i = 1; i < 4; i++)
   if ((((op)->spec >> ((i) - 1) * 2) & 0x03) == 0x02) imm_arg = i - 1;
  jit_op * newop = jit_op_new(JIT_FMOV | 0x02, (((0x00) << 4) | ((0x02) << 2) | (0x03)), (jit_value) (((((1)) & 0x01) | ((((1)) & 0x03) << 1) | ((0) & 0xfffffff) << 4)), 0, 0, 0);
  newop->fp = 1;
  newop->flt_imm = op->flt_imm;
  jit_op_prepend(op, newop);
  op->code &= ~(0x3);
  op->code |= 0x01;
  op->spec &= ~(0x3 << (2 * imm_arg));
  op->spec |= (0x01 << (2 * imm_arg));
  op->arg[imm_arg] = (((((1)) & 0x01) | ((((1)) & 0x03) << 1) | ((0) & 0xfffffff) << 4));
 }
}
static inline void jit_expand_patches_and_labels(struct jit * jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PATCH) {
   ((jit_op *)(op->arg[0]))->jmp_addr = op;
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_LABEL) {
   ((jit_label *)(op->arg[0]))->op = op;
  }
  if ((((jit_opcode) (op->code & 0xfff8)) != JIT_LABEL) && (jit_is_label(jit, (void *)op->arg[0]))) {
   op->jmp_addr = ((jit_label *)(op->arg[0]))->op;
  }
  if ((((jit_opcode) (op->code & 0xfff8)) != JIT_LABEL) && (jit_is_label(jit, (void *)op->arg[1]))) {
   op->jmp_addr = ((jit_label *)(op->arg[1]))->op;
  }
 }
}
static inline void jit_prepare_reg_counts(struct jit * jit)
{
 int declared_args = 0;
 int last_gp = -1;
 int last_fp = -1;
 int gp_args = 0;
 int fp_args = 0;
 struct jit_func_info * info = NULL;
 jit_op * op = jit_op_first(jit->ops);
 while (1) {
  if (!op || (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG)) {
   if (info) {
    info->gp_reg_count = last_gp + 1;
    info->fp_reg_count = last_fp + 1;
    info->general_arg_cnt = gp_args;
    info->float_arg_cnt = fp_args;
    info->args = malloc(sizeof(struct jit_inp_arg) * declared_args);
   }
   if (op) {
    declared_args = 0;
    last_gp = -1;
    last_fp = -1;
    gp_args = 0;
    fp_args = 0;
    info = (struct jit_func_info *)op->arg[1];
   }
   if (!op) break;
  }
  for (int i = 0; i < 3; i++)
   if (((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x03) || ((((op)->spec >> ((i + 1) - 1) * 2) & 0x03) == 0x01)) {
    jit_reg r = (jit_reg) op->arg[i];
    if ((((r) & 0x01) == (0)) && ((((r) >> 4) & 0xfffffff) > last_gp)) last_gp = (((r) >> 4) & 0xfffffff);
    if ((((r) & 0x01) == (1)) && ((((r) >> 4) & 0xfffffff) > last_fp)) last_fp = (((r) >> 4) & 0xfffffff);
   }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DECL_ARG) {
   declared_args++;
   if (op->arg[0] == JIT_FLOAT_NUM) fp_args++;
   else gp_args++;
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PREPARE) {
   jit_op * xop = op;
   while (1) {
    if (((jit_opcode) (op->next->code & 0xfff8)) == JIT_PUTARG) xop->arg[0]++;
    else if (((jit_opcode) (op->next->code & 0xfff8)) == JIT_FPUTARG) xop->arg[1]++;
    else {
     jit_opcode next_code = ((jit_opcode) (op->next->code & 0xfff8));
     if (next_code == JIT_CALL) break;
     if ((next_code != JIT_TRACE) && (next_code != JIT_CODE_ALIGN)
     && (next_code != JIT_UREG) && (next_code != JIT_LREG)
     && (next_code != JIT_RENAMEREG) && (next_code != JIT_SYNCREG))
     {
      printf("Garbage in the prepare-call block. Opcode: %x\n", next_code >> 3);
      abort();
     }
    }
    op = op->next;
   }
  }
  op = op->next;
 }
}
static inline void jit_prepare_arguments(struct jit * jit)
{
 jit_op * op = jit_op_first(jit->ops);
 struct jit_func_info * info = NULL;
 int gp_arg_pos = 0;
 int fp_arg_pos = 0;
 int argpos = 0;
 int phys_reg = 0;
 while (op) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) {
   info = (struct jit_func_info *)op->arg[1];
   info->has_prolog = 1;
   gp_arg_pos = 0;
   fp_arg_pos = 0;
   argpos = 0;
   phys_reg = 0;
  }
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DECL_ARG) {
   info->args[argpos].type = op->arg[0];
   info->args[argpos].size = op->arg[1];
   if (op->arg[0] == JIT_FLOAT_NUM) {
    info->args[argpos].gp_pos = gp_arg_pos;
    info->args[argpos].fp_pos = fp_arg_pos++;
   } else {
    info->args[argpos].gp_pos = gp_arg_pos++;
    info->args[argpos].fp_pos = fp_arg_pos;
   }
   jit_init_arg_params(jit, info, argpos, &phys_reg);
   argpos++;
  }
  op = op->next;
 }
}
static inline void jit_prepare_spills_on_jmpr_targets(struct jit *jit)
{
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next)
  if ((((jit_opcode) (op->code & 0xfff8)) == JIT_REF_CODE) || (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE)) {
   jit_op * newop = jit_op_new(JIT_FULL_SPILL | 0x02, (((0x00) << 4) | ((0x00) << 2) | (0x00)), 0, 0, 0, 0);
   jit_op_prepend(op->jmp_addr, newop);
  }
}
static inline void jit_buf_expand(struct jit * jit)
{
 long pos = jit->ip - jit->buf;
 jit->buf_capacity *= 2;
 jit->buf = realloc(jit->buf, jit->buf_capacity);
 jit->ip = jit->buf + pos;
}
void jit_generate_code(struct jit * jit)
{
 jit_expand_patches_and_labels(jit);
 jit_correct_float_imms(jit);
 jit_prepare_reg_counts(jit);
 jit_prepare_arguments(jit);
 jit_prepare_spills_on_jmpr_targets(jit);
 if (jit->optimizations & (0x08)) {
  jit_dead_code_analysis(jit, 1);
 }
 jit_flw_analysis(jit);
 if (jit->optimizations & (0x02)) jit_optimize_unused_assignments(jit);
 int change = 0;
 jit_optimize_st_ops(jit);
 if (jit->optimizations & (0x04)) {
  change |= jit_optimize_join_addmul(jit);
  change |= jit_optimize_join_addimm(jit);
 }
 if (change) jit_flw_analysis(jit);
 jit_collect_statistics(jit);
 jit_assign_regs(jit);
 if (jit->optimizations & (0x01)) jit_optimize_frame_ptr(jit);
 jit->buf_capacity = (4096);
 jit->buf = malloc(jit->buf_capacity);
 jit->ip = jit->buf;
 for (struct jit_op * op = jit->ops; op != NULL; op = op->next) {
  if (jit->buf_capacity - (jit->ip - jit->buf) < (1024)) jit_buf_expand(jit);
  unsigned long offset_1 = (jit->ip - jit->buf);
  switch (((jit_opcode) (op->code & 0xfff8))) {
   case JIT_DATA_BYTE: *(jit->ip)++ = (unsigned char) op->arg[0]; break;
   case JIT_DATA_BYTES:
    for (int i = 0; i < op->arg[0]; i++)
     *(jit->ip)++ = *(((unsigned char *) op->addendum) + i);
    break;
   case JIT_DATA_REF_CODE:
   case JIT_DATA_REF_DATA:
    op->patch_addr = ((jit_value)jit->ip - (jit_value)jit->buf);
    for (int i = 0; i < sizeof(void *); i++) {
     *jit->ip = 0;
     jit->ip++;
    }
    break;
   case JIT_FORCE_SPILL:
   case JIT_FORCE_ASSOC:
   case JIT_COMMENT:
   case JIT_MARK:
   case JIT_TOUCH:
    break;
   default: jit_gen_op(jit, op);
  }
  unsigned long offset_2 = (jit->ip - jit->buf);
  op->code_offset = offset_1;
  op->code_length = offset_2 - offset_1;
 }
 int code_size = jit->ip - jit->buf;
 void *mem = mmap(NULL, jit->buf_capacity, PROT_READ | PROT_EXEC | PROT_WRITE, MAP_ANON | MAP_PRIVATE, -1, 0);
 if (mem == MAP_FAILED) perror("mmap");
 memcpy(mem, jit->buf, code_size);
 free(jit->buf);
 long pos = jit->ip - jit->buf;
 jit->buf = mem;
 jit->ip = jit->buf + pos;
 jit->mmaped_buf = 1;
 jit_patch_external_calls(jit);
 jit_patch_local_addrs(jit);
 for (jit_op * op = jit_op_first(jit->ops); op != NULL; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG)
   *(void **)(op->arg[0]) = jit->buf + (long)op->patch_addr;
 }
}
void jit_trace(struct jit *jit, int verbosity)
{
 for (jit_op *op = jit_op_first(jit->ops)->next; op != NULL; op = op->next) {
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_PROLOG) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_BYTE) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_CODE) continue;
  if (((jit_opcode) (op->code & 0xfff8)) == JIT_DATA_REF_DATA) continue;
  jit_op * o = jit_op_new(JIT_TRACE, (((0x00) << 4) | ((0x00) << 2) | (0x02)), verbosity, 0, 0, 0);
  o->r_arg[0] = o->arg[0];
  jit_op_prepend(op, o);
 }
}
static void jit_internal_free_ops(struct jit_op * op)
{
 if (op == NULL) return;
 jit_internal_free_ops(op->next);
 if (op->addendum) free(op->addendum);
 jit_free_op(op);
}
static void jit_internal_free_labels(jit_label * lab)
{
 if (lab == NULL) return;
 jit_internal_free_labels(lab->next);
 free(lab);
}
static int jit_internal_is_cond_branch_op(jit_op *op)
{
 jit_opcode code = ((jit_opcode) (op->code & 0xfff8));
 return (code == JIT_BLT) || (code == JIT_BLE) || (code == JIT_BGT)
 || (code == JIT_BGE) || (code == JIT_BEQ) || (code == JIT_BNE)
 || (code == JIT_FBLT) || (code == JIT_FBLE) || (code == JIT_FBGT)
 || (code == JIT_FBGE) || (code == JIT_FBEQ) || (code == JIT_FBNE)
 || (code == JIT_BOADD) || (code == JIT_BOSUB) || (code == JIT_BNOADD)
 || (code == JIT_BNOSUB);
}
void jit_enable_optimization(struct jit * jit, int opt)
{
 jit->optimizations |= opt;
}
void jit_disable_optimization(struct jit * jit, int opt)
{
 jit->optimizations &= ~opt;
}
void jit_free(struct jit * jit)
{
 jit_reg_allocator_free(jit->reg_al);
 jit_internal_free_ops(jit_op_first(jit->ops));
 jit_internal_free_labels(jit->labels);
 if (jit->buf) {
  if (jit->mmaped_buf) munmap(jit->buf, jit->buf_capacity);
  else free(jit->buf);
 }
 free(jit);
}
int jit_regs_active_count(jit_op *op)
{
 return jit_set_size(op->live_out);
}
void jit_regs_active(jit_op *op, jit_value *dest)
{
 jit_set_to_array(op->live_out, dest);
}
void jit_message(struct jit * j, char * s) {
  jit_add_op(j, JIT_MSG | 0x02, (((0x00) << 4) | ((0x00) << 2) | (0x02)), (jit_value)(s), 0, 0, 0, jit_debug_info_new("head.c", __func__, 19));
}
void jit_messager(struct jit * j, char * s, int i) {
  jit_add_op(j, JIT_MSG | 0x01, (((0x00) << 4) | ((0x01) << 2) | (0x02)), (jit_value)(s), (((((0)) & 0x01) | ((((0)) & 0x03) << 1) | (((i)) & 0xfffffff) << 4)), 0, 0, jit_debug_info_new("head.c", __func__, 23));
}
